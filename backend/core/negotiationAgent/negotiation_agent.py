from crewai import LLM, Agent, Task, Crew, Process
from core.llm_services.mistral_api import MistralAPI
from .helper import create_negotiation_prompt

class Negotiation_Agent:
    def __init__(self):
        mistral_api = MistralAPI()
        mistral_api.setModel("mistral/mistral-large-latest")
        self.llm = LLM(model=str(mistral_api))
        self.conversation_history = []
        self.best_offer = None

    def negotiator(self) -> Agent:
        return Agent(
            role="Negotiator as the buyer",
            goal="Negotiate the best deal for the user based on constraints and available negotiation tactics. Pay attention to user goals (e.g., budget, quality) if provided. Also always calculate the best deal based on the budget and the price for one unit of the product. Don't mention about your budget to the vendor. Your goal is trying to find a better deal that fits your budget as well.",
            backstory="You are an expert at negotiating product deals and finding the best deals according to the available information.",
            llm=self.llm
        )

    def negotiation_task(self, deals, user_constraints, quantity, quantity_type) -> Task:
        return Task(
            description=create_negotiation_prompt(deals, user_constraints, quantity, quantity_type),
            expected_output="Return the chatbot's response for negotiation.",
            agent=self.negotiator()
        )

    def build(self, deals, user_constraints, quantity, quantity_type) -> Crew:
        return Crew(
            agents=[self.negotiator()],
            tasks=[self.negotiation_task(deals, user_constraints, quantity, quantity_type)],
            process=Process.sequential
        )

    def start_conversation(self, product_name, brand, Price, max_budget, order_quantity, unit):
        self.conversation_history.append({
            "role": "Negotiator as the buyer",
            "content": create_negotiation_prompt(product_name, brand, Price, max_budget, order_quantity, unit)
        })
        return self.get_response()

    def continue_conversation(self, vendor_response):
        self.conversation_history.append({
            "role": "vendor",
            "content": vendor_response
        })
        return self.get_response()

    def get_response(self):
        task = Task(
            description="\n".join([f"{msg['role']}: {msg['content']}" for msg in self.conversation_history]),
            expected_output="Return the chatbot's response as for negotiation as the buyer. Also, provide the explanation for agent's action. Provide that as a JSON. Fields should be Response and Explanation.",
            agent=self.negotiator()
        )
        crew = Crew(
            agents=[self.negotiator()],
            tasks=[task],
            process=Process.sequential
        )
        response = crew.kickoff().raw
        self.conversation_history.append({
            "role": "negotiator as the buyer",
            "content": response
        })
        self.add_summary()
        return response

    def finalize_negotiation(self, vendor_response):
        self.conversation_history.append({
            "role": "negotiator as the buyer",
            "content": "Thank you for your final offer. The negotiation has ended."
        })
        return "Thank you for your final offer. The negotiation has ended."

    def add_summary(self):
        summary_agent = Agent(
            role="Summarizer",
            goal="Summarize the conversation between the buyer and the vendor.",
            backstory="You are an expert at summarizing conversations.",
            llm=self.llm
        )
        summary_task = Task(
            description="\n".join([f"{msg['role']}: {msg['content']}" for msg in self.conversation_history]),
            expected_output="Provide a concise summary of the conversation.",
            agent=summary_agent
        )
        summary_crew = Crew(
            agents=[summary_agent],
            tasks=[summary_task],
            process=Process.sequential
        )
        summary_response = summary_crew.kickoff().raw
        self.conversation_history = [{
            "role": "summary",
            "content": summary_response
        }]

    def summarize_conversation(self):
        summary = "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.conversation_history if msg['role'] == 'summary'])
        final_decision = self.conversation_history[-1]['content'] if self.conversation_history else "No final decision."
        return {
            "summary": summary,
            "final_decision": final_decision
        }
