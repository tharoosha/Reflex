from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.negotiationAgent.negotiation_agent import Negotiation_Agent

router = APIRouter()

class NegotiationRequest(BaseModel):
    message: str

negotiation_agent = Negotiation_Agent()
chat_history = []

@router.post("/negotiation")
async def negotiate(request: NegotiationRequest):
    try:
        bot_response = negotiation_agent.continue_conversation(request.message)
        chat_history.append({"user": request.message, "bot": bot_response})
        return {"bot_response": bot_response, "chat_history": chat_history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
