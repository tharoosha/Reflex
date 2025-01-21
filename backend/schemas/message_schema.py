from pydantic import BaseModel

class MessageInput(BaseModel):
    message: str
    user_mobile_no: str


class SendMessageInput(BaseModel):
    recipient: str  # Phone number in international format (e.g., +1234567890)
    message: str    # Message text to send