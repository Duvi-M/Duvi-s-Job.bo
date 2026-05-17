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

## Auth

Create a candidate, company user, or company admin:

```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "candidate@example.com",
    "password": "strong-password",
    "full_name": "Candidate User",
    "role": "candidate"
  }'
```

Public registration is intentionally blocked for `platform_admin`.

Log in:

```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "candidate@example.com",
    "password": "strong-password"
  }'
```

Use the returned bearer token:

```bash
curl http://localhost:8000/auth/me \
  -H "Authorization: Bearer <access_token>"
```

## Migrations

```bash
alembic upgrade head
```

Current migration: `20260517_0001_create_users_table.py`.

## Tests

```bash
pytest
```
