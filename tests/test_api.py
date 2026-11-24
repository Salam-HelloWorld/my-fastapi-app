import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.store import store

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_store():
    store.clear()
    yield
    store.clear()


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_crud_flow():
    r = client.post("/items", json={"name": "Book", "price": 12.5})
    assert r.status_code == 201
    item = r.json()
    assert item == {"id": 1, "name": "Book", "description": None, "price": 12.5, "in_stock": True}

    assert client.get("/items").json() == [item]
    assert client.get("/items/1").json() == item

    r = client.patch("/items/1", json={"price": 10, "in_stock": False})
    assert r.status_code == 200
    assert r.json()["price"] == 10
    assert r.json()["in_stock"] is False
    assert r.json()["name"] == "Book"

    assert client.delete("/items/1").status_code == 204
    assert client.get("/items/1").status_code == 404


def test_not_found():
    assert client.get("/items/99").status_code == 404
    assert client.patch("/items/99", json={"price": 1}).status_code == 404
    assert client.delete("/items/99").status_code == 404


def test_validation():
    assert client.post("/items", json={"name": "", "price": 1}).status_code == 422
    assert client.post("/items", json={"name": "X", "price": -1}).status_code == 422


def test_swagger_docs_available():
    r = client.get("/docs")
    assert r.status_code == 200
    assert "swagger-ui" in r.text
    schema = client.get("/openapi.json").json()
    assert "/items" in schema["paths"]














def test_config_hides_secret(monkeypatch):
    monkeypatch.setenv("APP_NAME", "Test App")
    monkeypatch.setenv("WELCOME_MESSAGE", "Hello test")
    monkeypatch.setenv("API_SECRET", "super-secret-value")

    r = client.get("/config")
    assert r.status_code == 200
    body = r.json()
    assert body["app_name"] == "Test App"
    assert body["welcome_message"] == "Hello test"
    assert body["api_secret_configured"] is True
    assert "super-secret-value" not in r.text
    assert "api_secret" not in body
