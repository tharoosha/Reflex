from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.negotiationAgent.negotiation_agent import Negotiation_Agent
import json

router = APIRouter()

class NegotiationRequest(BaseModel):
    message: str

negotiation_agent = Negotiation_Agent()
chat_history = []

@router.post("/negotiation/start")
async def negotiate(request: NegotiationRequest):
    try:
        with open("../negotiation_details.json", "r") as file:
            result = json.load(file)
        start_response = negotiation_agent.start_conversation(result['product_name'], result['brand'], result['Price'], result['max_budget'], result['order_quantity'], result['unit'])
        print("start_response is", start_response)
        return {"bot_response": start_response, "chat_history": chat_history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/negotiation/continue")
async def negotiate(request: NegotiationRequest):
    try:
        bot_response = negotiation_agent.continue_conversation(request.message)
        chat_history.append({"user": request.message, "bot": bot_response})
        return {"bot_response": bot_response, "chat_history": chat_history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
