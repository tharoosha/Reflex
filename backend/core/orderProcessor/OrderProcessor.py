
from core.comparisonAgent import Comparison_Agent
from core.shoppingAgent import Shopping_Agent

class OrderProcessor:
    
    def __init__(self):
        self.comparisonAgent = Comparison_Agent()
        self.shoppingAgent = Shopping_Agent()
        self

    def process_order(self, product_name, quantity, quantity_type):
        deals = self.shoppingAgent.get_deals(product_name)
        results = self.comparisonAgent.compare(**kwargs)
        return results