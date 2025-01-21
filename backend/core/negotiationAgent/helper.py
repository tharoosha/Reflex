
from db.aiven_connection import get_connection

def create_negotiation_prompt(product_name, brand, Price, max_budget, order_quantity, unit):
    # constraints_text = "\n".join([f"- {key}: {value}" for key, value in constraints.items()])
    # deals_text = "\n".join([f"{i}. {deal}" for i, deal in enumerate(deals)])

    return f"""
    Analyze below deal:

    Product Name: {product_name}
    Brand: {brand}
    Price: {Price}
    Max Budget: {max_budget}
    Required Quantity: {order_quantity} {unit}
        
    Negotiate the best deal that matches these constraints.
    As the buyer you start the negotiation with the vendor with greetings and telling your purpose. But don't tell about the budget to the vendor. Ultimate goal is to get the best price that fit to our budget from the vendor.
    """


