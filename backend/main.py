from controllers.user_controller import router as user_router
from controllers.iot_controller import router as iot_router
from controllers.message_controller import router as message_router
from fastapi import FastAPI
import uvicorn
from pyngrok import ngrok, conf

# Initialize the FastAPI app
app = FastAPI(
    title="Reflex Backend",
    version="1.0.0",
)

# Include the routers
app.include_router(user_router, prefix="/api")
app.include_router(iot_router, prefix="/api")
app.include_router(message_router, prefix="/api")  # Uncommented to include this router

# Start ngrok tunnel and run the app
if __name__ == "__main__":
    try:
        # Run the app with Uvicorn
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print("Shutting down ngrok tunnel...")

