import json
from core.prompt.test_prompt import ExamplePrompt
from core.utils.api_utils import APIUtils


class TestService:
    """
    Class to check if a show test service class.
    """

    def __init__(self, model_name: str = "mistral-7b", api_type: str = 'openrouter'):
        """
        Initialize the AnswerChecker with the specified model.
        """
        self.api_utils = APIUtils(model_name=model_name, api_type=api_type)

    def testing(self, question: str):
        """
        Check if the user's answer is correct compared to the expected answer.
        """
        prompt = ExamplePrompt.construct(question)
        response = self.api_utils.generate_response(prompt)
        print(response)
        return response




