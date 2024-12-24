import json
from backend.app.core.prompt.test_prompt import ExamplePrompt
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

    def testing(self, question: str, expected_answer: str, user_answer: str):
        """
        Check if the user's answer is correct compared to the expected answer.
        """
        prompt = ExamplePrompt.construct(question, expected_answer, user_answer)
        response = self.api_utils.generate_response(prompt)
        return self.api_utils.parse_json_response(response)




