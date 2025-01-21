from controllers.user_controller import router as user_router
from controllers.iot_controller import router as iot_router
from controllers.negotiation_controller import router as negotiation_router  # Add this line
from fastapi import FastAPI
import uvicorn

# Initialize the FastAPI app
app = FastAPI(
    title="Reflex Backend",
    version="1.0.0",
)

# Include the routers
app.include_router(user_router, prefix="/api")
app.include_router(iot_router, prefix="/api")
app.include_router(negotiation_router, prefix="/api")

# Run the app with Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
