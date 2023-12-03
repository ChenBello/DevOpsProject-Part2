# pip install pytest
# pip install fastapi uvicorn pytest

# test_pastapi_app.py:

import requests
from fastapi.testclient import TestClient
import pytest
from app.fastapi_app import app


# Define a fixture for the test client
@pytest.fixture
def test_client():
    return TestClient(app)


# Define the test for profile registration
def test_register_profile(test_client, monkeypatch, caplog):
    # Mock the requests.post method to simulate interaction with Spring Boot
    def mock_post(url, json):
        assert url == "http://localhost:8080/register"
        assert json["fullName"] == "John Doe"

        # Create a mock response with a valid status code (e.g., 200) and HTML content
        response = requests.Response()
        response.status_code = 200
        response._content = b'<html><head></head><body><p>Successfully registered profile: John Doe</p></body></html>'

        return response

    monkeypatch.setattr(requests, 'post', mock_post)

    # Simulate registering a profile and interacting with the Spring Boot server
    response = test_client.post("/register", json={"fullName": "John Doe"})

    assert response.status_code == 200
    assert "Successfully registered profile: John Doe" in response.text
