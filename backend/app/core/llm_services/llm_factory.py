# from mistral_api import MistralAPI
from .mistral_api import MistralAPI
from .openrouter_api import OpenRouterAPI

class LLMFactory:
    """
    Factory to create instances of different LLM APIs.
    """

    @staticmethod
    def get_llm(api_type: str, config: dict = None):
        """
        Return the appropriate LLM instance based on `api_type`.
        """
        if api_type == "mistral":
            return MistralAPI()
        elif api_type == "openrouter":
            if not config:
                raise ValueError("OpenAI requires a configuration dictionary.")
            return OpenRouterAPI(
                model_name=config["name"]
            )
        else:
            raise ValueError(f"Unsupported API type: {api_type}")
