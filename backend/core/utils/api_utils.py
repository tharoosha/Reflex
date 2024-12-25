# from openai import OpenAI
import openai
from typing import Dict
from models.model_registry import ModelRegistry
import json
from core.llm_services.llm_factory import LLMFactory

class APIUtils:
    """
    Utility class for interacting with different LLM APIs.
    """

    def __init__(self, model_name: str, api_type: str):
        """
        Initialize APIUtils for a specific model.
        """
        self.model_config = ModelRegistry.get_model_config(model_name)
        self.api_type = api_type

    def generate_response(self, prompt: str) -> str:
        """
        Call the LLM API to get a response for the given prompt.
        """
        # response = openai.ChatCompletion.create(
        #     model=self.model_config["name"],
        #     messages=[{"role": "user", "content": prompt}]
        # )
        llm = LLMFactory.get_llm(self.api_type, self.model_config if self.api_type=="openrouter" else None)
        response = llm.generate_response(prompt)
        return response

    @staticmethod
    def parse_json_response(response: str) -> Dict:
        """
        Extract and parse the JSON from the response.
        """
        try:
            start_index = response.find('{')
            end_index = response.rfind('}') + 1
            json_text = response[start_index:end_index]
            return json.loads(json_text)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON: {e}")
