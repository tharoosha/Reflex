from core.logic.nlp_processor import NLPProcessor
from db.local_db_temp import user_preferences_store


def process_nl_input(query: str):
    nlprocessor=NLPProcessor()
    nlprocessor.process_input(query)
    return "nl data processed successfully"



# Hardcode the user ID
HARDCODED_USER_ID = "1"

def save_user_preferences(preferences: dict):
    """
    Save user preferences to the in-memory store.
    The user ID is hardcoded in this function.
    """
    # Check if the user ID exists
    if HARDCODED_USER_ID not in user_preferences_store:
        # If not, create a new list for the user
        user_preferences_store[HARDCODED_USER_ID] = []

    # Append the new preferences to the user's list
    user_preferences_store[HARDCODED_USER_ID].append(preferences)

    print(f"Preferences saved for user {HARDCODED_USER_ID}: {user_preferences_store[HARDCODED_USER_ID]}")
    return {"message": f"Preferences saved successfully for user {HARDCODED_USER_ID}"}
