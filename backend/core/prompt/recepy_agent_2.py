PROMPT_TEMPLATE = """You are a culinary expert with extensive knowledge of global cuisines. Your task is to provide a detailed shopping list for preparing the specified dish. The shopping list should include all necessary ingredients along with their precise quantities. Please format your response as a JSON object following this structure:

{{
  "dish": "Dish Name",
  "shopping_list": [
    ("Ingredient 1", "Quantity 1"),
    ("Ingredient 2", "Quantity 2"),
    ...
  ]
}}

Dish to prepare: {nl_input}"""