# from fastapi import APIRouter, Request, Response
# from twilio.twiml.messaging_response import MessagingResponse

# from core.services.message_service import whatsapp_message_service

# router = APIRouter(prefix="/messages", tags=["Messages"])

# @router.api_route("/receive", methods=["GET", "POST"])
# async def incoming_sms(request: Request):
#     # Parse incoming data
#     body = None
#     if request.method == "POST":
#         form_data = await request.form()
#         body = form_data.get("Body", None)
#     elif request.method == "GET":
#         query_params = request.query_params
#         body = query_params.get("Body", None)

#     # Log the incoming message
#     print(f"Received message: {body}")

#     # Create a TwiML response
#     resp = MessagingResponse()
#     result=whatsapp_message_service(body)
#     resp.message(result)

#     # Return the TwiML response to Twilio
#     return Response(content=str(resp), media_type="application/xml")
