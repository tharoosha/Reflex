# from dotenv import load_dotenv
# import os

# load_dotenv()

# openrouter_api_key = os.environ["OPENROUTER_API_KEY"]

class ModelRegistry:
    """
    Registry for multiple models and their configurations.
    """

    MODELS = {
        "gemini": {
            "name": "google/gemini-2.0-flash-exp:free",
        },
        "mistral-7b": {
            "name": "mistralai/mistral-7b-instruct:free",
        },
        "phi3-mini": {
            "name": "microsoft/phi-3-mini-128k-instruct:free",
        },
        "phi3-medium": {
            "name": "microsoft/phi-3-medium-128k-instruct:free",
        },
        "learnlm": {
            "name": "google/learnlm-1.5-pro-experimental:free",
        },
    }

    @classmethod
    def get_model_config(cls, model_name: str) -> dict:
        """
        Retrieve model configuration by name.
        """
        if model_name not in cls.MODELS:
            raise ValueError(f"Model '{model_name}' not found in the registry.")
        return cls.MODELS[model_name]
