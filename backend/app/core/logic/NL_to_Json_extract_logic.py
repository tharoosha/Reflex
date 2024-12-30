import time

from backend.app.core.Agent.NL_to_Json_extract_agent import NLPAgent
from backend.app.core.llm_services.mistral_api import MistralAPI
from backend.app.core.logic.business_logic import Analyzer
from backend.app.core.prompt.NL_to_Json_extract_agent_template import PROMPT_TEMPLATE


class NLPProcessor:
    def __init__(self):
        mistral_api = MistralAPI()  # Create an instance of MistralAPI
        self.analyzer=Analyzer()
        mistral_id, mistral_api_key = mistral_api.getNameAndAPIKey()
        self.nlp_agent = NLPAgent(mistral_id, mistral_api_key, PROMPT_TEMPLATE)

    def process_input(self, nl_input: str) -> str:
        prompt = PROMPT_TEMPLATE.format(nl_input=nl_input)
        json_object=self.nlp_agent.process_input(prompt)
        # print(json_object)
        return self.analyzer.append_to_list(json_object)


if __name__ == "__main__":

    nlp_processor = NLPProcessor()
    example_input = "Order 10 coffee pods when stock is below 10. Order 5 milk when stock is equal 5."

    output = nlp_processor.process_input(example_input)
    print(output)
