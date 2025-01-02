from abc import ABC, abstractmethod

class ShoppingPrompt(ABC):
    
    @abstractmethod
    def apply(self, **kwargs)->str:
        pass

class VanilaSearch(ShoppingPrompt):
    prompt = """
    ##
    Task: Search the Database and List the matching products to the given input and output matching products in the given  JSON output format.

    ##
    Format of the Input: 
    [
      product_name : String|None (Name of the product to search),
      product_variations : String|None (Variations of the product if applicable),
    ]
    
    ##
    Output: Json Array Object with the Structure:
    JSONArrayObject (
        JSONObject (
            product_name : String (Name of the product),
            product_variations : String (Variations of the product),
            product_price : Float (Price of the product),
            product_discount : Float (Discount on the product),
            product_discount_type : Int (Type_id of discount on the product),
            )
        JSONObject()
        JSONObject()
    )
    
    ##
    Input :
    [
        product_name : {name},
        product_variations : {variations}
    ]
    """
    
    def apply(self, **kwargs)->str:
        
        product_name = kwargs.get("product_name")
        product_variations = kwargs.get("product_variations")
        return self.prompt.format(name = product_name, variations = product_variations)

class QueryGenerator(ShoppingPrompt):
    
    prompt = """
    ##
    Task: Generate a SQL Query to search the Database for the given input and output the SQL Query in the given Format.

    ##
    Format of the Input: 
    [
      product_name : String|None (Name of the product to search),
      product_variations : String|None (Variations of the product if applicable),
      preferences : String|None (Preferences of the user),
      dislikes : String|None (Dislikes of the user),
    ]

    ##
    SQL Query Format: (search, omit)
    SELECT product_id, product_name, product_variation,
       MATCH(product_name, product_variation) AGAINST('search - omit' IN boolean mode) AS relevance
        FROM Product
            WHERE MATCH(product_name, product_variation) AGAINST('search - omit' IN boolean mode)
            ORDER BY relevance DESC;
    
    ##
    Example Input :
    [
        product_name : Coffee,
        product_variations : Instant,
        preferences : Nescafe,
        dislikes : Bru
    ]

    ##
    Example Output:
    SELECT product_id, product_name, product_variation,
       MATCH(product_name, product_variation) AGAINST('Coffee Instant Nescafe - Bru' IN boolean mode) AS relevance
        FROM Product
            WHERE MATCH(product_name, product_variation) AGAINST('Coffee Instant Nescafe - Bru' IN boolean mode)
            ORDER BY relevance DESC;

    ## Input :
    [
        product_name : {name},
        product_variations : {variations},
        preferences : {preferences},
        dislikes : {dislikes}
    ]
    """
    
    def apply(self, **kwargs)->str:
        
        product_name = kwargs.get("product_name", "None")
        product_variations = kwargs.get("product_variations", "None")
        preferences = kwargs.get("preferences", "None")
        dislikes = kwargs.get("dislikes", "None")
        return self.prompt.format(name = product_name, variations = product_variations, preferences = preferences, dislikes = dislikes)