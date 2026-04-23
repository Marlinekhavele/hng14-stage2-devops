from unittest.mock import patch


import pytest
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def mock_redis():
    with patch("api.main.r") as mock:
        mock.lpush.return_value = None
        mock.hset.return_value = None
        mock.hget.return_value = None
        yield mock


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_create_job():
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()


def test_get_job_not_found():
    response = client.get("/jobs/invalid")
    assert response.status_code == 404
