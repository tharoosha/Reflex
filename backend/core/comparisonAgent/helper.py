from backend.core.logic.sql_processor import SQLProcessor
from db.aiven_connection import get_connection

def create_prompt_with_context(deals, constraints):
    constraints_text = "\n".join([f"- {key}: {value}" for key, value in constraints.items()])
    deals_text = "\n".join([f"{i}. {deal}" for i, deal in enumerate(deals)])
    discounts = DBAgent().search()
    discounts_text = "\n".join([f"{i}. {discount}" for i, discount in enumerate(discounts)])

    return f"""
    Analyze these deals: 
    {deals_text}
    
    Consider these user constraints:
    {constraints_text}

    These are the details of the different possible discounts:
    {discounts_text}
    
    Find the best deal that matches these constraints.
    Return the best deal as a JSONObject. Don't output anything at all.
    """

class DBAgent():
    query = """SELECT Discount_Type, Description, Rule  FROM Discount;"""
    
    def __init__(self):
        self.connection = get_connection()
        self.model = SQLProcessor(tool_names = ['SQLTool'], enable_tools=True)
    
    def search(self):
        response = None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(self.query)
                response = cursor.fetchall()
        finally:
            self.connection.close()
        return response




