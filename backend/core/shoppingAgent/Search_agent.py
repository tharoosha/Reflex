from abc import ABC, abstractmethod
from .Shopping_Prompt import VanilaSearch, QueryGenerator
from core.logic.sql_processor import SQLProcessor
from core.logic.nlp_processor import NLPProcessor
from db.aiven_connection import get_connection

class SearchAgent(ABC):

    @abstractmethod
    def search(self, **kwargs):
        pass

class LLMAgent(SearchAgent):
    
    def __init__(self):
        self.propt_agent = VanilaSearch()
        self.model = SQLProcessor(tool_names = ['SQLTool'], enable_tools=True)
    
    def search(self, **kwargs):
        prompt = self.propt_agent.apply(**kwargs)
        response = self.model.process_input(prompt)
        return response

class QueryAgent(SearchAgent):
    
    def __init__(self):
        self.connection = get_connection()
        self.model = NLPProcessor()
        self.propt_agent = QueryGenerator()
    
    def search(self, **kwargs):
        prompt = self.propt_agent.apply(**kwargs)
        response = self.model.process_input(prompt, template=False)
        return response

class DBAgent(SearchAgent):
    
    query = """
    SELECT 
        p.product_id, 
        p.product_name, 
        p.brand,
        p.product_variation, 
        p.description, 
        p.attributes, 
        p.ingrediants,
        p.price,
        p.product_rating,
        p.MFD,
        p.EXP,
        p.Quantity,
        p.Quantity_type,
        p.contains,
        p.free_from,
        p.best_seller,
        MATCH(p.brand, p.product_name, p.product_variation, p.attributes, p.ingrediants, p.free_from) 
        AGAINST('{brand} {product} {product_variation} {preferences} free_from:{allergies} -{dislikes} -ingredients:{allergies}' IN boolean mode) AS relevance
    FROM Product p
    WHERE MATCH(p.brand, p.product_name, p.product_variation, p.attributes, p.ingrediants, p.free_from) 
        AGAINST('{brand} {product} {product_variation} free_from:{allergies} -{dislikes} -ingredients:{allergies}' IN boolean mode)
    ORDER BY relevance DESC;

    """
    def __init__(self):
        self.connection = get_connection()
        self.model = SQLProcessor(tool_names = ['SQLTool'], enable_tools=True)

    def escape_single_quotes(self, value):
            return value.replace("'", "''") if value else value
    
    def search(self, **kwargs):
        brand = self.escape_single_quotes(kwargs.get("brand", "None"))
        product = self.escape_single_quotes(kwargs.get("product", "None"))
        preferences = self.escape_single_quotes(kwargs.get("preferences", "None"))
        product_variation = self.escape_single_quotes(kwargs.get("product_variation", "None"))
        allergies = self.escape_single_quotes(kwargs.get("allergies", "None"))
        dislikes = self.escape_single_quotes(kwargs.get("dislikes", "None"))
        query = self.query.format(brand=brand, product=product, preferences=preferences, product_variation=product_variation,
                                  allergies=allergies, dislikes=dislikes)
        response = None
        try:
            # Create a cursor object
            with self.connection.cursor() as cursor:
                
                # Execute the SQL query
                cursor.execute(query)
                
                # Fetch all the results
                response = cursor.fetchall()

        finally:
            # Close the connection
            self.connection.close()
        return response