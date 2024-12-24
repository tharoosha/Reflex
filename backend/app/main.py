from fastapi import FastAPI
from backend.app.controllers.test_controller import router as test_router
import uvicorn

app = FastAPI(
    title="Reflex Backend",
    version="1.0.0",
)

# Include the Socratic Tutor router
app.include_router(test_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Socratic Tutor API!"}

# Run the app with Uvicorn and reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)