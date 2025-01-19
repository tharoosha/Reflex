# from controllers.user_controller import router as user_router
# from controllers.iot_controller import router as iot_router
# from fastapi import FastAPI
# import uvicorn

# Initialize the FastAPI app
# app = FastAPI(
#     title="Reflex Backend",
#     version="1.0.0",
# )

# Include the routers
# app.include_router(user_router, prefix="/api")
# app.include_router(iot_router, prefix="/api")

# Run the app with Uvicorn
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# Example use case for negotiation agent
from core.negotiationAgent.negotiation_agent import Negotiation_Agent

if __name__ == "__main__":
    deals = [
        {"product_id": 1, "product_name": "Coffee", "brand": "Imperial", "price": 10}
    ]
    user_constraints = {"budget": 8, "brand": "Imperial", "product_name": "Coffee"}
    quantity = 200
    quantity_type = "Grams"

    negotiation_agent = Negotiation_Agent()
    bot_response = negotiation_agent.start_conversation(deals, user_constraints, quantity, quantity_type)
    print("===========================Starting negotiation===========================")
    print("Bot:", bot_response)

    while True:
        vendor_response = input("Vendor: ")
        if vendor_response.lower() in ["final offer", "accept", "decline"]:
            print("Negotiation ended.")
            bot_response = negotiation_agent.fainalize_negotiation(vendor_response)
            print("Bot:", bot_response)
            summary = negotiation_agent.summarize_conversation()
            print("Summary of the conversation:")
            print(summary["summary"])
            print("Final decision:")
            print(summary["final_decision"])
            print("==================================negotiation is done=======================================")
            break
        bot_response = negotiation_agent.continue_conversation(vendor_response)
        print("Bot:", bot_response)
        print("------------------------------------------------------")
