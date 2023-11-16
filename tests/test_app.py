"""
Application Testing
--------------------
"""
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_default():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "active"} 
