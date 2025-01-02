from crewai import LLM, Agent, Task, Crew, Process
from core.llm_services.mistral_api import MistralAPI
from .helper import create_prompt_with_context

class Deal_Finding_Agent:
    def __init__(self):
        mistral_api = MistralAPI()
        mistral_api.setModel("mistral/mistral-large-latest")
        self.llm = LLM(model=str(mistral_api))

    def deal_finder(self) -> Agent:
        return Agent(
            role="Deal Finder",
            goal="Find the best deal for the user based on constraints and available discounts. Pay attention to user goals (e.g., budget, quality) if provided.",
            backstory="You are an expert at analyzing product deals and finding the best match for user requirements.",
            llm=self.llm
        )

    def deal_finding_task(self, deals, user_constraints, quantity, quantity_type) -> Task:
        return Task(
            description=create_prompt_with_context(deals, user_constraints, quantity, quantity_type),
            expected_output=
            """
                Return the product_id for the best deal.
                ## Example Output (JSON) 1:
                    {
                        "product_id": 5,
                        "product_name": "Coffee",
                        "brand": "Imperial",
                        "product_variation": "Dark Roast",
                        "Quantity": 200,
                        "Quantity_type": "Grams",
                        "Price": 10,
                        "reson_of_choice": "Has a 20% discount user provided he is looking for a budget option."
                    }
                
                ## Example Output (JSON) 2:
                    {
                        "product_id": 5,
                        "product_name": "Coffee",
                        "brand": "Nescafe",
                        "product_variation": "Dark Roast",
                        "Quantity": 200,
                        "Quantity_type": "Grams",
                        "Price": 30,
                        "reason_of_choice": "User prefers premium quality and is willing to pay more."
                    }
            """,
            agent=self.deal_finder()
        )

    def build(self, deals, user_constraints, quantity, quantity_type) -> Crew:
        return Crew(
            agents=[self.deal_finder()],
            tasks=[self.deal_finding_task(deals, user_constraints, quantity, quantity_type)],
            process=Process.sequential
        )



