from fastapi.testclient import TestClient
from app.main import app
from app.config import settings

# checken status code van de key
#code 200 of 401

#check content type --> bytes

client = TestClient(app)

def test_response_200():
    response = client.get("/screenshots", params={"url": "https://thomasmore.be/en", "width": 1280, "height": 720} ,headers={"X-API-Key": settings.API_KEYS})
    assert response.status_code == 200

def test_response_401():
    response = client.get("/screenshots", params={"url": "https://thomasmore.be/en", "width": 1280, "height": 720} ,headers={"X-API-Key": "fake_key_123"})
    assert response.status_code == 401


