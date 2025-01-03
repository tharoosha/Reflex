from fastapi import APIRouter, Request, HTTPException
from core.services.user_service import process_nl_input, save_user_preferences
from schemas.user_schema import UserPreferences

router = APIRouter()

@router.post("/user/nl-process")  # Ensure the route starts with a `/`
async def nl_process_controller(request: Request):
    try:
        # Read the JSON input directly
        body = await request.json()
        query = body.get("query")

        # Validate query input
        if not query or query== "":
            raise HTTPException(status_code=400, detail={"error": "No query provided in the request"})

        # Process the query
        process_nl_input(query)

        # Return success response
        return {"message": "NL data processed successfully"}
    except Exception as e:
        # Log and return an error response
        print(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail={"error": str(e)})

@router.post("/user/preferences")
async def set_user_preferences(preferences: UserPreferences):
    try:
        response = save_user_preferences(preferences.model_dump())
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))