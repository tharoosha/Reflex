from crewai import LLM, Agent, Task, Crew, Process
from core.llm_services.mistral_api import MistralAPI
from .helper import create_prompt_with_context

class Deal_Finding_Agent:
    def __init__(self, deals, user_constraints):
        mistral_api = MistralAPI()
        mistral_api.setModel("mistral/mistral-large-latest")
        self.llm = LLM(model=str(mistral_api))
        self.deals = deals
        self.user_constraints = user_constraints

    def deal_finder(self) -> Agent:
        return Agent(
            role="Deal Finder",
            goal="Find the best deal for the user based on constraints and available discounts.",
            backstory="You are and expert at analyzing product deals and finding the best match for user requirements.",
            llm=self.llm
        )

    def deal_finding_task(self) -> Task:
        return Task(
            description=create_prompt_with_context(self.deals, self.user_constraints),
            expected_output=
            """
                Return the product_id for the best deal.
                ## Example Output format:
                    {
                        "product_id": 5,
                        "product_name": "Coffee",
                        "brand": "Imperial",
                        "product_variation": "Dark Roast",
                        "description": "A full-bodied dark roast coffee with notes of chocolate and caramel.",
                        "attributes": null,
                        "ingrediants": "100% Arabica coffee beans, Caffaine",
                        "price": 15.99,
                        "product_rating": 4.2,
                        "MFD": "2024-11-01",
                        "Quantity": 200,
                        "Quantity_type": "Grams",
                        "contains": "Coffee",
                        "free_from": "Gluten",
                        "best_seller": "Yes",
                        "relevance": 0.1812381148338318
                    }
            """,
            agent=self.deal_finder()
        )

    def build(self) -> Crew:
        return Crew(
            agents=[self.deal_finder()],
            tasks=[self.deal_finding_task()],
            process=Process.sequential
        )



