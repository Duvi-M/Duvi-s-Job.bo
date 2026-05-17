# Backend

FastAPI backend for Duvi's Job.bo.

## Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

## Health Check

```bash
curl http://localhost:8000/health
```

## Migrations

```bash
alembic revision --autogenerate -m "create initial tables"
alembic upgrade head
```

## Tests

```bash
pytest
```

