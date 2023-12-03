#  app/fastapi_app.py:
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests
import logging

app = FastAPI(debug=True)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ProfileRequest(BaseModel):
    fullName: str


@app.post("/register", response_class=HTMLResponse)
async def register_profile(profile_request: ProfileRequest):
    # Simulate interaction with the Spring Boot server
    spring_boot_url = "http://localhost:8080/register"

    # Prepare data to send to Spring Boot server
    data = {
        "fullName": profile_request.fullName,
    }

    try:
        # Make a POST request to the Spring Boot server
        response = requests.post(spring_boot_url, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Log the successful interaction
        logger.info(f"Successfully registered profile: {profile_request.fullName}")

        # If successful, return a simple HTML response
        return HTMLResponse(
            content=f"<html><head></head><body><p>Successfully registered profile: {profile_request.fullName}</p></body></html>")

    except requests.RequestException as e:
        # Log the error
        logger.error(f"Error interacting with Spring Boot server: {str(e)}")

        # Raise an HTTPException with a custom error message
        raise HTTPException(status_code=500, detail="Internal server error during registration")


if __name__ == "__main__":
    import uvicorn

    # Run the application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
