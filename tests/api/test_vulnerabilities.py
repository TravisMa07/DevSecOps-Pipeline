import pytest


def test_list_vulnerabilities_returns_empty_list(client):
    response = client.get("/vulnerabilities")
    assert response.status_code == 200
    assert response.json() == {"vulnerabilities": []}


def test_create_and_get_vulnerability(client):
    payload = {
        "id": "vuln-2",
        "description": "This is another test vulnerability.",
        "severity": "medium",
        "cvss_score": 5.0,
        "cvss_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L",
        "discovered_date": "2026-09-16",
        "exploitable": False,
        "fix_available": True,
        "mitigation_steps": "Update the software to the latest version.",
        "note": "This vulnerability is not exploitable.",
    }

    create_response = client.post("/vulnerabilities", json=payload)
    assert create_response.status_code == 201, create_response.json()
    get_response = client.get(f"/vulnerabilities/{payload['id']}")
    assert get_response.status_code == 200, get_response.json()
    assert get_response.json() == {"vulnerability": payload}

    list_response = client.get("/vulnerabilities")
    assert list_response.status_code == 200, list_response.json()
    assert list_response.json() == {"vulnerabilities": [payload]}


def test_get_nonexistent_vulnerability_returns_404(client):
    response = client.get("/vulnerabilities/nonexistent-id")
    assert response.status_code == 404
    assert response.json() == {"detail": "Vulnerability not found"}


def test_create_duplicate_vulnerability_returns_400(client):
    payload = {
        "id": "vuln-2",
        "description": "This is another test vulnerability.",
        "severity": "medium",
        "cvss_score": 5.0,
        "cvss_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L",
        "discovered_date": "2026-09-16",
        "exploitable": False,
        "fix_available": True,
        "mitigation_steps": "Update the software to the latest version.",
        "note": "This vulnerability is not exploitable.",
    }

    create_response = client.post("/vulnerabilities", json=payload)
    assert create_response.status_code == 201, create_response.json()

    duplicate_payload = {
        **payload,
        "description": "Attempt to overwrite the original record",
    }
    duplicate_response = client.post(
        "/vulnerabilities",
        json=duplicate_payload,
    )
    assert duplicate_response.status_code == 400, duplicate_response.json()
    assert duplicate_response.json() == {
        "detail": f"Vulnerability with ID {payload['id']} already exists."
    }
    get_response = client.get(f"/vulnerabilities/{payload['id']}")
    assert get_response.status_code == 200
    assert get_response.json() == {"vulnerability": payload}


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("severity", "High"),
        ("cvss_score", -0.1),
        ("cvss_score", 10.1),
        ("discovered_date", "not-a-date"),
        ("id", ""),
        ("description", ""),
    ],
)
def test_invalid_vulnerability_returns_422(client, field, value):
    payload = {
        "id": "invalid-test",
        "description": "Test vulnerability",
        "severity": "medium",
        "cvss_score": 5.0,
        "discovered_date": "2026-09-16",
        "exploitable": False,
        "fix_available": True,
    }
    payload[field] = value

    response = client.post("/vulnerabilities", json=payload)

    assert response.status_code == 422, response.json()
    assert any(error["loc"] == ["body", field] for error in response.json()["detail"])

    list_response = client.get("/vulnerabilities")
    assert list_response.status_code == 200
    assert list_response.json() == {"vulnerabilities": []}


def test_missing_required_field_returns_422(client):
    payload = {
        "id": "missing-field-test",
        "description": "Test vulnerability",
        # Required severity is intentionally omitted.
        "cvss_score": 5.0,
        "discovered_date": "2026-09-16",
        "exploitable": False,
        "fix_available": True,
    }

    response = client.post("/vulnerabilities", json=payload)

    assert response.status_code == 422, response.json()
    assert any(
        error["loc"] == ["body", "severity"] and error["type"] == "missing"
        for error in response.json()["detail"]
    )
