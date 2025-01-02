from core.logic.sql_processor import SQLProcessor
from .Shopping_Prompt import VanilaSearch
from .Search_agent import QueryAgent
from db.aiven_connection import get_connection

class Shopping_Agent():
    
    def __init__(self):

        self.connection = get_connection()
        self.model = SQLProcessor(tool_names = ['SQLTool'], enable_tools=True)
        self.propt_agent = QueryAgent()
    
    def search(self, product_name, proct_variations, preferences, Dislikes):
        prompt = self.propt_agent.search(product_name = product_name, product_variations = proct_variations, 
                                        preferences = preferences, dislikes = Dislikes)
        return prompt
    
    def get_search_prompt(self, product_name, proct_variations):
        return self.propt_agent.apply(product_name = product_name, product_variations = proct_variations)