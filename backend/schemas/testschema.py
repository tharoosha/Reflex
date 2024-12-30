from pydantic import BaseModel
from typing import List, Dict, Optional


class TesModel(BaseModel):
    """
    Request model for Socratic Tutor API.
    """
    question: str



