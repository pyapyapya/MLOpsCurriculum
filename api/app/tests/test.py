import pytest
from fastapi.testclient import TestClient

from main import app

test_client = TestClient(app)


@pytest.mark.asyncio
async def test_healthcheck():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == "OK"
