# local_db_nl = {
#     "order_list": {},  # Stores order-related data
#     "recipy_list": {},  # Stores recipy-related data
#     "time_trigger_list": {}  # Stores time trigger data
# }


# Temporary in-memory storage for user preferences
user_preferences_store = {}

local_db_nl = {
    "order_list": {
        "customer_123": {
            "coffee pods": {
                "product_type": "coffee pods",
                "quantity": 5,
                "threshold": "<5",
                "specific_time_period": None,
                "re_order_after": None
            },
            "milk": {
                "product_type": "milk",
                "quantity": 3,
                "threshold": "<3",
                "specific_time_period": None,
                "re_order_after": None
            }
        },
        "customer_456": {
            "tea": {
                "product_type": "tea",
                "quantity": 20,
                "threshold": "<10",
                "specific_time_period": None,
                "re_order_after": None
            }
        }
    },
    "recipy_list": {
        "customer_123": {
            "recipe_1": {
                "recipe_name": "coffee latte",
                "ingredients": ["coffee pods", "milk", "sugar"]
            },
            "recipe_2": {
                "recipe_name": "black coffee",
                "ingredients": ["coffee pods", "water"]
            }
        },
        "customer_456": {
            "recipe_1": {
                "recipe_name": "masala tea",
                "ingredients": ["tea", "milk", "spices"]
            }
        }
    },
    "time_trigger_list": {
        "customer_123": {
            "trigger_1": {
                "trigger_name": "morning_coffee",
                "time": "08:00",
                "action": "brew coffee latte"
            }
        },
        "customer_456": {
            "trigger_1": {
                "trigger_name": "evening_tea",
                "time": "18:00",
                "action": "prepare masala tea"
            }
        }
    }
}

local_db_iot={

}