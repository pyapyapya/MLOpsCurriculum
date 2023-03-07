import json

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from ..main import app
from crud import crud_user
test_client = TestClient(app)


@pytest.mark.asyncio
async def test_healthcheck():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == "OK", "Not Health Checked"


@pytest.mark.asyncio
async def test_create_user():
    response = test_client.post("/users",
    json={
        "name": "user1",
        "age": 120
        }
    )

    assert response.json() == {
        "id": 1,
        "name": "user1",
        "age": 120
    }


@pytest.mark.asyncio
async def test_get_user():
    response = test_client.get("/users/{id}", params={"id": "1"})
    assert response.json() == {
        "id": 1,
        "name": "user1",
        "age": 120
    }
