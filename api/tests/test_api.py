from unittest.mock import patch


import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def mock_redis():
    with patch("api.main.r", autospec=True) as mock_redis:
        mock_redis.lpush.return_value = None
        mock_redis.hset.return_value = None
        mock_redis.hget.return_value = None
        yield mock_redis


def test_health():
    res = client.get("/health")
    assert res.status_code == 200


def test_create_job(mock_redis):
    mock_redis.hset.return_value = None
    res = client.post("/jobs")
    assert res.status_code == 200
    assert "job_id" in res.json()


def test_get_job_not_found(mock_redis):
    mock_redis.hget.return_value = None
    res = client.get("/jobs/invalid")
    assert res.status_code == 404
