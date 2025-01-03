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
            "coffee": {
                "product_type": "coffee",
                "quantity": 10,
                "threshold": "<5",
                "specific_time_period": None,
                "re_order_after": None,
                "Unit": "pods"
            },
            "milk": {
                "product_type": "milk",
                "quantity": 5,
                "threshold": "<3",
                "specific_time_period": None,
                "re_order_after": None,
                "Unit": "liters"
            }
        },
        "customer_456": {
            "tea": {
                "product_type": "tea",
                "quantity": 10,
                "threshold": "<10",
                "specific_time_period": None,
                "re_order_after": None,
                "Unit": "bags"
            }
        }
    },
    "recipy_list": {
        "customer_123": {
            "recipe_1": {
                "recipe_name": "coffee latte",
                "ingredients": ["coffee", "milk", "sugar"]
            },
            "recipe_2": {
                "recipe_name": "black coffee",
                "ingredients": ["coffee", "water"]
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