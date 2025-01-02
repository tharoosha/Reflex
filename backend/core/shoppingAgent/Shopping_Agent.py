from .Search_agent import DBAgent

class Shopping_Agent():
    
    def __init__(self):

        self.propt_agent = DBAgent()
    
    def search(self, **kwargs):
        results = self.propt_agent.search(**kwargs)
        return results