from core.logic.business_logic import order_comparing_function


def process_iot_data(data: dict):
    print("in process_iot_data")
    return order_comparing_function(data)