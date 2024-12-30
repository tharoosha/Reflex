from fastapi import APIRouter, HTTPException
from backend.app.schemas.testschema import TesModel
from core.logic.business_logic import testing_logic

router = APIRouter()


# In-memory conversation storage
conversations = {}

# API Endpoint: Handles the request and calls the core logic
@router.post("/api/testing", response_model=TesModel)
def socratic_tutor_endpoint(request: TesModel):
    try:
        # Call the core logic function
        response_data = testing_logic(request.user_prompt)
        return {"json": response_data}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

