# agent.py

from phi.agent import Agent
from phi.model.mistral import MistralChat


class MistralAgent:
    def __init__(self, model_id: str,api_key : str, prompt_template: str, tools: list = None):
        """
        Initialize the MistralAgent with the model, API key, prompt template, and tools.

        :param model_id: The ID of the Mistral model to use.
        :param api_key: API key for accessing the Mistral model.
        :param prompt_template: Template to guide the agent's behavior.
        :param tools: List of tools the agent can use.
        """
        self.agent = Agent(
            name="Mistral Agent",
            model=MistralChat(id=model_id, api_key=api_key),
            instructions=[prompt_template],
            tools=tools or [],
            show_tool_calls=True,
            markdown=True,
        )

    def generate(self, prompt: str) -> str:
        """
        Process the input prompt using the agent and return the response.

        :param prompt: The input string to process.
        :return: The agent's response as a string.
        """
        response = self.agent.run(prompt)
        return response.content
