PROMPT_TEMPLATE = """
You are given an input that may contain multiple situations. Each situation belongs to exactly one of these categories:
- 'order_related'
- 'recipy_related'
- 'time_trigger'

Your task is to:
1. Identify each situation from the input.
2. Classify each situation into the correct category.
3. Extract each situation into the JSON format for that category.

Guidelines for each category’s JSON format:

- **order_related**: Use this structure
    [
        {{
            "product_type": "string",       # Name of the product (e.g., "coffee pods", "milk")
            "quantity": integer/null,       # Quantity of the product (e.g., 10). Use null if not specified.
            "threshold": "string/null",     # Operator-based threshold (e.g., "<10", ">5", "=20", "≤5", "≥3"). 
                                            # Convert any textual expression like "below 10" to "<10". 
                                            # Use null if not specified.
            "specific_time_period": "string/null",  # Period for ordering (e.g., "weekly"). Use null if not specified.
            "re_order_after": "string/null"         # Time frame for reordering (e.g., "every 2 weeks"). Use null if not specified.
        }}
    ]

- **recipy_related**: Use this structure
    [
        {{
            "occasion": "string",    # The event or occasion (e.g., "New Year party", "weekend breakfast")
            "meal": "string/null",   # The type of meal (e.g., "breakfast", "dinner"). Use null if not specified.
            "use": "string"          # Indicates whether to use "existing ingredients" or "new ingredients"
        }}
    ]

- **time_trigger**: Use this structure
    [
        {{
            "occasion": "string",    # The timing or trigger event (e.g., "daily", "every night 9 PM")
            "action": "string",      # The action to perform (e.g., "notify", "check")
            "about": "string",       # The specific item or topic (e.g., "milk level", "low stock")
            "product": "string"      # The name of the product related to the trigger (e.g., "milk", "coffee pods")
        }}
    ]

Important Notes:
1. **Only include data that actually appears in the input.** If the user did not mention a particular product or threshold, set it to null.
2. **Do not use items from the example if they are not in the input.** The example is only to show the format.
3. **If a category is not mentioned at all**, still include that category in the final JSON, but with an empty array.
4. **Combine all categorized objects** into one JSON object with three top-level keys: "order_related", "recipy_related", and "time_trigger".
5. **Only the Json object, Don't include the input or any other text.

### Converting threshold expressions to operators
- "below X", "under X", "less than X"  => "<X"
- "above X", "more than X", "over X"   => ">X"
- "exactly X", "equal to X"            => "=X"
- If you need “at most X” or “no more than X” => "≤X"
- If you need “at least X” or “no less than X” => "≥X"

If the user’s wording doesn’t clearly map to an operator or they give a range, represent it in a concise operator-based format (e.g., "10–20", "<5–10", etc.) as best as you can.

### Input:
{nl_input}

### Output:
A single JSON object with the structure:
{{ "order_related": [...], "recipy_related": [...], "time_trigger": [...] }}

where each array only contains items **actually** mentioned in the input. If the user’s input does not mention a category, return an empty array for that category.
"""


