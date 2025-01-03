from typing import List

from pydantic import BaseModel

# Input Schema for NL processing
class NLInput(BaseModel):
    query: str  # Natural language query as a string


class UserPreferences(BaseModel):
    preferred_brands: List[str]
    dietary_restrictions: List[str]
    max_budget: float
    delivery_priority: str
    autonomy: bool