from fastapi import FastAPI
# from controllers.test_controller import router as test_router
import uvicorn
from core.services.testing_chat import TestService  # Import TestService

app = FastAPI(
    title="Reflex Backend",
    version="1.0.0",
)

# Include the Socratic Tutor router
# app.include_router(test_router)

# Initialize the TestService
test_service = TestService()

@app.get("/")
def root():
    # Test the TestService with a hardcoded question
    test_message = "What is the capital of France?"
    response = test_service.testing(test_message)
    return {
        "message": "Welcome to the RefleX Replenishment Service!",
        "test_message": test_message,
        "test_response": response
    }

# Run the app with Uvicorn and reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)