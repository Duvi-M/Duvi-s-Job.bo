# Architecture

## Overview

Duvi's Job.bo uses a monorepo with separate frontend and backend applications. The first scaffold keeps boundaries clear while staying lightweight enough for fast MVP iteration.

## Applications

- `frontend`: Next.js application with TypeScript and Tailwind CSS.
- `backend`: FastAPI application with SQLAlchemy, PostgreSQL, Alembic, and pytest.
- `infra`: infrastructure assets and deployment notes.
- `docs`: product and engineering documentation.

## Backend Structure

```text
backend/app/
├── api/             # FastAPI routers
├── core/            # settings, database, shared infrastructure
├── models/          # SQLAlchemy models
├── schemas/         # Pydantic schemas
├── services/        # business logic
├── repositories/    # data access patterns
└── tests/           # pytest tests
```

## Data

PostgreSQL is the system of record. SQLAlchemy will own models and database sessions. Alembic will manage migrations.

## Local Development

Docker Compose starts PostgreSQL and can run the backend and frontend. Developers can also run each app directly for faster feedback.

