import os
from mistralai import Mistral
from .llm_interfaces import LLMBase
from dotenv import load_dotenv
import os

load_dotenv()
class MistralAPI(LLMBase):
    """
    Implementation of the Mistral API.
    """

    def __init__(self):
        self.api_key = os.environ["MISTRAL_API_KEY"]
        self.client = Mistral(api_key=self.api_key)
        self.model = "mistral-large-latest"

    def generate_response(self, prompt: str) -> str:
        chat_response = self.client.chat.complete(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return chat_response.choices[0].message.content
