# main.py

import os
from core.agent.nl_to_json_extract_agent import NLPAgent
from core.llm_services.mistral_api import MistralAPI
from core.prompt.nl_to_json_extract_agent_template import PROMPT_TEMPLATE


class NLPProcessor:
    def __init__(self):
        mistral_api = MistralAPI()  # Create an instance of MistralAPI
        mistral_id, mistral_api_key = mistral_api.getNameAndAPIKey()
        self.nlp_agent = NLPAgent(mistral_id, mistral_api_key, PROMPT_TEMPLATE)

    def process_input(self, nl_input: str) -> str:
        prompt = PROMPT_TEMPLATE.format(nl_input=nl_input)
        return self.nlp_agent.process_input(prompt)



