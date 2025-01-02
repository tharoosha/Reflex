from abc import ABC, abstractmethod
from .Shopping_Prompt import VanilaSearch, QueryGenerator
from core.logic.sql_processor import SQLProcessor
from core.logic.nlp_processor import NLPProcessor
from db.aiven_connection import get_connection

class SearchAgent(ABC):

    @abstractmethod
    def search(self, **kwargs):
        pass

class LLMAgent(SearchAgent):
    
    def __init__(self):
        self.propt_agent = VanilaSearch()
        self.model = SQLProcessor(tool_names = ['SQLTool'], enable_tools=True)
    
    def search(self, **kwargs):
        prompt = self.propt_agent.apply(**kwargs)
        response = self.model.process_input(prompt)
        return response

class QueryAgent(SearchAgent):
    
    def __init__(self):
        self.connection = get_connection()
        self.model = NLPProcessor()
        self.propt_agent = QueryGenerator()
    
    def search(self, **kwargs):
        prompt = self.propt_agent.apply(**kwargs)
        response = self.model.process_input(prompt, template=False)
        return response