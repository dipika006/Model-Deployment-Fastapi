from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World"}


def test_get_name():
    response = client.get("/abcd")
    assert response.status_code == 200
    assert response.json() == {"Welcome To Second page": "abcd"}


def test_predict_banknote_pass():
    data = {"variance": 0.1, "skewness": 0.2, "curtosis": 0.3, "entropy": 0.6}
    response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json() == {"prediction": "Fake note"}


def test_predict_banknote_fail():
    data = {
        "variance": 0,
        "skewness": 0,
        "curtosis": 0,
    }
    response = client.post("/predict", json=data)
    assert response.status_code == 422
