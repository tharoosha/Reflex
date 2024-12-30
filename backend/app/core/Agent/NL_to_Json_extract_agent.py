from phi.agent import Agent
from phi.model.mistral import MistralChat


class NLPAgent:
    def __init__(self, model_id: str,api_key : str, prompt_template: str):
        self.agent = Agent(
            name="NLP Processor Agent",
            model=MistralChat(id=model_id, api_key=api_key),
            instructions=[prompt_template],
            show_tool_calls=True,
            markdown=True,
        )

    def process_input(self, prompt: str) -> str:
        response = self.agent.run(prompt)
        return response.content
