from core.agent.mistral_agent import MistralAgent
from core.agent.tool_registry import ToolRegistry
from core.llm_services.mistral_api import MistralAPI


class SQLProcessor:
    def __init__(self, tool_names: list = None, enable_tools=False):
        """
        Initialize the NLPProcessor with optional tool support.

        :param tool_names: List of tools to initialize (e.g., ["SQLTool", "SearchTool"]).
        """
        mistral_api = MistralAPI()
        mistral_id, mistral_api_key = mistral_api.getNameAndAPIKey()
        
        if enable_tools:
            # Initialize tools dynamically based on provided tool names
            tools = ToolRegistry.get_tools(tool_names) if tool_names else []

            self.nlp_agent = MistralAgent(mistral_id, mistral_api_key, prompt_template="", tools=tools)

    def process_input(self, nl_input: str) -> str:
        """
        Process natural language input through the agent.

        :param nl_input: Natural language input string.
        :return: The agent's response.
        """
        prompt = f"Process this input: {nl_input}"
        return self.nlp_agent.generate(prompt)
