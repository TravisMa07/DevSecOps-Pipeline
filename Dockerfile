FROM python:3.13
WORKDIR /app

COPY pyproject.toml .
COPY src ./src

RUN python -m pip install --upgrade pip
RUN python -m pip install .

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]