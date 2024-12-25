from abc import ABC, abstractmethod

class LLMBase(ABC):
    """
    Abstract base class for LLM APIs.
    """

    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the LLM.
        """
        pass
