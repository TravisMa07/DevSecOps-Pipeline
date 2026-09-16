from fastapi import APIRouter, HTTPException
from app.models.vulnerability import Vulnerability
from app.services import vulnerability_service

router = APIRouter(
    prefix="/vulnerabilities", tags=["vulnerabilities"]
)

@router.get("")
def list_vulnerabilities():
    records = vulnerability_service.list_vulnerabilities()
    return {"vulnerabilities": records}

@router.get("/{vulnerability_id}")
def get_vulnerability(vulnerability_id: str):
    record = vulnerability_service.get_vulnerability(vulnerability_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    return {"vulnerability": record}

@router.post("", status_code=201)
def create_vulnerability(vulnerability: Vulnerability):
    try:
        record = vulnerability_service.create_vulnerability(vulnerability)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"vulnerability": record}