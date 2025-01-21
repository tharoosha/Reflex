from core.services.user_service import process_nl_input


def whatsapp_message_service(message):
    return process_nl_input(message)