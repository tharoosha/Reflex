import json

# from core.orderProcessor.processor import OrderProcessor
from db.local_db_temp import local_db_nl  # Import the local store

def get_order_processor():
    from core.orderProcessor.processor import OrderProcessor
    return OrderProcessor()

def append_to_local_db(prompt_json):

    # Hardcode customer ID for now
    customer_id = "customer_1234"

    # Ensure the customer ID exists in the local database
    if customer_id not in local_db_nl["order_list"]:
        local_db_nl["order_list"][customer_id] = {}
    if customer_id not in local_db_nl["recipy_list"]:
        local_db_nl["recipy_list"][customer_id] = {}
    if customer_id not in local_db_nl["time_trigger_list"]:
        local_db_nl["time_trigger_list"][customer_id] = {}

    # Clean and parse the JSON input
    prompt_json = str(prompt_json)
    clean_json = prompt_json.strip("```json").strip("```").strip()
    parsed_json = json.loads(clean_json)

    # Update order_list in local_db for this customer
    for order in parsed_json.get("order_related", []):
        product_type = order["product_type"]
        # Replace the product type if it already exists
        local_db_nl["order_list"][customer_id][product_type] = order

    # Update recipy_list in local_db for this customer
    for recipy in parsed_json.get("recipy_related", []):
        recipe_name = recipy.get("recipe_name", f"recipe_{len(local_db_nl['recipy_list'][customer_id]) + 1}")
        local_db_nl["recipy_list"][customer_id][recipe_name] = recipy

    # Update time_trigger_list in local_db for this customer
    for trigger in parsed_json.get("time_trigger", []):
        trigger_name = trigger.get("trigger_name", f"trigger_{len(local_db_nl['time_trigger_list'][customer_id]) + 1}")
        local_db_nl["time_trigger_list"][customer_id][trigger_name] = trigger

    print("Local DB updated successfully for customer:", customer_id)
    print(json.dumps(local_db_nl, indent=4))






def order_comparing_function(IoT_Json):

    # Hardcode customer ID for now
    customer_id = "customer_123"  # Replace with dynamic logic as needed

    # Check if the customer exists in the local database
    if customer_id not in local_db_nl["order_list"]:
        print(f"Customer ID {customer_id} not found in the database.")
        return

    # Extract the product details from IoT JSON
    product = IoT_Json.get("product_type")
    remaining = IoT_Json.get("remaining")
    unit=IoT_Json.get("unit")

    print(f"Product : {product}")
    print(f"Remaining: {remaining}")

    # Check if the product exists in the customer's order list
    if product in local_db_nl["order_list"][customer_id]:
        order = local_db_nl["order_list"][customer_id][product]
        threshold = order.get("threshold")
        order_quantity=order.get("quantity")
        if threshold and isinstance(threshold, str):
            operator, value = threshold[0], float(threshold[1:])
            if (operator == "<" and remaining < value) or (operator == "=" and remaining <= value) or (operator == "≤" and remaining <= value):
                order_processor = get_order_processor()
                result=order_processor.process_order(product, "None", order_quantity, unit)

                negotiation_details = {
                    "product_name": result['product_name'],
                    "brand": result['brand'],
                    "Price": result['Price'],
                    "max_budget": result['max_budget'],
                    "order_quantity": order_quantity,
                    "unit": unit
                }

                with open("../negotiation_details.json", "w") as json_file:
                    json.dump(negotiation_details, json_file, indent=4)

    else:
        # If the product type is not found, check the remaining quantity
        if remaining == 0:
            print(f"Product {product} is out of stock! Triggering an order.")

        else:
            print(f"Product {product} not found in the database for customer {customer_id}.")



# Example for testing
if __name__ == "__main__":
    # JSON input with extra annotations
    raw_json = """```json
    {
      "order_related": [
        {
          "product_type": "coffee pods",
          "quantity": 10,
          "threshold": "<10",
          "specific_time_period": null,
          "re_order_after": null
        },
        {
          "product_type": "milk",
          "quantity": 5,
          "threshold": "<5",
          "specific_time_period": null,
          "re_order_after": null
        }
      ],
      "recipy_related": [],
      "time_trigger": []
    }
    ```"""
    append_to_local_db(raw_json)

    # Example IoT JSON inputs to test
    iot_json_1 = {
        "product": "coffee pods",
        "remaining": 9
    }

    iot_json_2 = {
        "product": "milk",
        "remaining": 6
    }

    iot_json_3 = {
        "product": "milk",
        "remaining": 4
    }

    iot_json_4 = {
        "product": "tea",
        "remaining": 0
    }

    print("\nTesting IoT JSON 1:")
    order_comparing_function(iot_json_1)

    print("\nTesting IoT JSON 2:")
    order_comparing_function(iot_json_2)

    print("\nTesting IoT JSON 3:")
    order_comparing_function(iot_json_3)

    print("\nTesting IoT JSON 4:")
    order_comparing_function(iot_json_4)
