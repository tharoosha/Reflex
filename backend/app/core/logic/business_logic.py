import json
import threading
import time


class Analyzer:
    def __init__(self):
        self.order_list=[]
        self.recipy_list=[]
        self.time_trigger_list=[]
        # self.running=False
        # self.start_periodic_task()

    def append_to_list(self,prompt_json):
        prompt_json=str(prompt_json)
        clean_json = prompt_json.strip("```json").strip("```").strip()
        parsed_json = json.loads(clean_json)
        self.order_list.extend(parsed_json.get("order_related", []))
        self.recipy_list.extend(parsed_json.get("recipy_related", []))
        self.time_trigger_list.extend(parsed_json.get("time_trigger", []))
        print(self.order_list,self.recipy_list,self.time_trigger_list)

    def order_comparing_function(self, IoT_Json):
        # Parse the IoT_Json input
        product_type = IoT_Json.get("product_type")
        amount = IoT_Json.get("amount")

        print(f"Product Type: {product_type}")
        print(f"Amount: {amount}")

        for order in self.order_list:
            if order["product_type"] == product_type:
                threshold = order.get("threshold")
                if threshold and isinstance(threshold, str):
                    operator, value = threshold[0], float(threshold[1:])
                    if operator == "<" and amount < value:
                        print(f"Amount of {product_type} ({amount}) is below the threshold ({threshold}).")
                    elif operator == ">" and amount > value:
                        print(f"Amount of {product_type} ({amount}) is above the threshold ({threshold}).")
                    elif operator == "=" and amount == value:
                        print(f"Amount of {product_type} ({amount}) matches the threshold ({threshold}).")
                    elif operator == "≤" and amount <= value:
                        print(f"Amount of {product_type} ({amount}) is at or below the threshold ({threshold}).")
                    elif operator == "≥" and amount >= value:
                        print(f"Amount of {product_type} ({amount}) is at or above the threshold ({threshold}).")
                break

    # def periodic_task(self):
    #     print("Periodic task triggered!")
    #
    #     #logic
    #     print("logic")
    #
    #     print(f"Order List: {self.order_list}")
    #     print(f"Recipy List: {self.recipy_list}")
    #     print(f"Time Trigger List: {self.time_trigger_list}")
    #
    # def start_periodic_task(self):
    #     self.running = True
    #
    #     def run_task():
    #         while self.running:
    #             self.periodic_task()
    #             time.sleep(10 )  # Wait for 10 minutes (600 seconds
    #
    #     thread = threading.Thread(target=run_task, daemon=True)
    #     thread.start()
    #
    # def stop_periodic_task(self):
    #     self.running = False


if __name__ == "__main__":
    analyzer = Analyzer()

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
    analyzer.append_to_list(raw_json)

    # Example IoT JSON inputs to test
    iot_json_1 = {
        "product_type": "coffee pods",
        "amount": 9
    }

    iot_json_2 = {
        "product_type": "milk",
        "amount": 6
    }

    iot_json_3 = {
        "product_type": "milk",
        "amount": 4
    }

    print("\nTesting IoT JSON 1:")
    analyzer.order_comparing_function(iot_json_1)

    print("\nTesting IoT JSON 2:")
    analyzer.order_comparing_function(iot_json_2)

    print("\nTesting IoT JSON 3:")
    analyzer.order_comparing_function(iot_json_3)
