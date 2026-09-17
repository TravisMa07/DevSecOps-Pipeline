from fastapi import FastAPI

from app.api.vulnerabilities import router

app = FastAPI(title="Vulnerability API")
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the vulnerability API!"}


@app.get("/health")
def health_check():
    return {"status": "OK"}
