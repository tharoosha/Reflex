
from db.aiven_connection import get_connection

def create_negotiation_prompt(deals, constraints, quantity, quantity_type):
    constraints_text = "\n".join([f"- {key}: {value}" for key, value in constraints.items()])
    deals_text = "\n".join([f"{i}. {deal}" for i, deal in enumerate(deals)])

    return f"""
    Analyze these deals: 
    {deals_text}
    
    Consider these user constraints:
    {constraints_text}

    Required Quantity: {quantity} {quantity_type}
    
    Negotiate the best deal that matches these constraints.
    As the buyer you start the negotiation with the vendor with greetings and telling your purpose. But don't tell about the budget to the vendor. Ultimate goal is to get the best price that fit to our budget from the vendor.
    """


