import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services import vulnerability_service


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(autouse=True)
def clear_vulnerabilities_storage():
    vulnerability_service._vulnerabilities.clear()
    yield
    vulnerability_service._vulnerabilities.clear()
