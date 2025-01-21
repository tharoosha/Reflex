
from core.comparisonAgent import Comparison_Agent
from core.shoppingAgent import Shopping_Agent
from core.userPreferences import UserPreferences
from core.reflexLogger import ConsoleLogger

class OrderProcessor:
    
    def __init__(self):
        self.comparisonAgent = Comparison_Agent()
        self.shoppingAgent = Shopping_Agent()
        self.userPreferences = UserPreferences()
        self.userPreferences.load_preferences()
        self.logger = ConsoleLogger()

    def process_order(self, product_name, product_variation ,quantity, quantity_type):
        user_constraints = self.userPreferences.get_product_preferences(product_name)
        user_constraints_msg = "User constraints for product: " + product_name + " are: " + user_constraints.__str__()
        self.logger.info(user_constraints_msg)

        if user_constraints is None:
            user_constraints = {}
        
        
        # TODO : Optimise the search function to take in user constraints
        deals = self.shoppingAgent.search(
            product=product_name, 
            product_variation=product_variation)

        deals_msg = "Deals found for product: " + product_name + "&"+ product_variation + " are: " + [deal['product_id'] for deal in deals].__str__()
        self.logger.info(deals_msg)
        
        results = self.comparisonAgent.get_best_deal(deals, user_constraints, quantity, quantity_type)
        results['max_budget'] = user_constraints['max_budget']
        result_product_id = results['product_id']
        result_reason = results['reason_of_choice']
        results_msg = "Best deal found for product: " + product_name + "&"+ product_variation + " is: " + str(result_product_id) + " with reason: " + result_reason
        self.logger.info(results_msg)
        return results