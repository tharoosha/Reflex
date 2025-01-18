import os
from google import genai
from .llm_interfaces import LLMBase
from dotenv import load_dotenv
import os

load_dotenv()

class MistralAPI(LLMBase):
    """
    Implementation of the Mistral API.
    """

    def __init__(self):
        self.api_key = os.environ["GEMINI_API_KEY"]
        self.client = genai.Client(api_key=self.api_key)
        self.model = self.client.GenerativeModel("gemini-1.5-flash")

    def generate_response(self, prompt: str) -> str:
        # chat_response = self.client.chat.complete(
        #     model=self.model,
        #     messages=[{"role": "user", "content": prompt}]
        # )
        return self.model.generate_content(prompt)
    
    def getNameAndAPIKey(self):
        return self.model, self.api_key