from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fibonacci_endpoint():
    response = client.get("/fibonacci/10")

    assert response.status_code == 200
    assert response.json() == {"result": 55}

def test_fibonacci_endpoint_invalid_input():
    response = client.get("/fibonacci/-1")

    assert response.status_code == 400
    assert response.json() == {
        "detail": "n must be greater than or equal to 0"
    }