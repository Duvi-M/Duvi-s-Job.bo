# Duvi's Job.bo

Duvi's Job.bo is a startup-style job marketplace foundation for Bolivia. The MVP will help candidates search and apply to jobs, companies publish openings, and platform admins review companies and jobs over time.

Current status: **Initial foundation / MVP scaffold**.

## Tech Stack

- Monorepo: `frontend`, `backend`, `infra`, `docs`
- Frontend: Next.js, TypeScript, Tailwind CSS
- Backend: FastAPI, Python, SQLAlchemy, Alembic
- Database: PostgreSQL
- Local development: Docker Compose
- Testing: pytest for backend, lint/typecheck scripts for frontend

## Folder Structure

```text
duvis-job-bo/
├── frontend/          # Next.js app
├── backend/           # FastAPI app
├── infra/             # Infrastructure notes and future deployment assets
├── docs/              # Product and engineering documentation
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## Run Locally

Copy the example environment file:

```bash
cp .env.example .env
```

Start PostgreSQL and the backend with Docker Compose:

```bash
docker compose up postgres backend
```

The backend will be available at:

```text
http://localhost:8000
```

Health check:

```bash
curl http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "service": "duvis-job-api"
}
```

To also start the frontend with Docker Compose:

```bash
docker compose up frontend
```

The frontend will be available at:

```text
http://localhost:3000
```

## Backend Development

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Run migrations after PostgreSQL is available:

```bash
alembic upgrade head
```

Auth endpoints are available under `/auth`:

- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`
- `GET /auth/admin-only-test`

## Frontend Development

```bash
cd frontend
npm install
npm run dev
```

## Tests

Backend:

```bash
cd backend
pytest
```

Frontend lint and typecheck:

```bash
cd frontend
npm run lint
npm run typecheck
```

## Next Ticket

Implement authentication and roles for `candidate`, `company_user`, `company_admin`, and `platform_admin`.
