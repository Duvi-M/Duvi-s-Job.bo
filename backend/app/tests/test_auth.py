from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.models.user import User, UserRole


def register_payload(
    email: str = "candidate@duvis.bo",
    role: str = "candidate",
) -> dict[str, str]:
    return {
        "email": email,
        "password": "strong-password",
        "full_name": "Candidate User",
        "role": role,
    }


def login(client: TestClient, email: str, password: str) -> str:
    response = client.post(
        "/auth/login",
        json={"email": email, "password": password},
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def test_user_registration_works(client: TestClient, db_session: Session) -> None:
    response = client.post("/auth/register", json=register_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "candidate@duvis.bo"
    assert data["full_name"] == "Candidate User"
    assert data["role"] == "candidate"
    assert "hashed_password" not in data

    user = db_session.query(User).filter_by(email="candidate@duvis.bo").one()
    assert user.hashed_password != "strong-password"
    assert user.hashed_password


def test_duplicate_email_registration_fails(client: TestClient) -> None:
    payload = register_payload()

    first_response = client.post("/auth/register", json=payload)
    second_response = client.post("/auth/register", json=payload)

    assert first_response.status_code == 201
    assert second_response.status_code == 409


def test_login_works_with_valid_credentials(client: TestClient) -> None:
    client.post("/auth/register", json=register_payload())

    response = client.post(
        "/auth/login",
        json={"email": "candidate@duvis.bo", "password": "strong-password"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["access_token"]
    assert data["token_type"] == "bearer"


def test_login_fails_with_wrong_password(client: TestClient) -> None:
    client.post("/auth/register", json=register_payload())

    response = client.post(
        "/auth/login",
        json={"email": "candidate@duvis.bo", "password": "wrong-password"},
    )

    assert response.status_code == 401


def test_auth_me_works_with_valid_token(client: TestClient) -> None:
    client.post("/auth/register", json=register_payload())
    token = login(client, "candidate@duvis.bo", "strong-password")

    response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    assert response.json()["email"] == "candidate@duvis.bo"
    assert "hashed_password" not in response.json()


def test_auth_me_fails_without_token(client: TestClient) -> None:
    response = client.get("/auth/me")

    assert response.status_code == 401


def test_candidate_cannot_access_admin_only_endpoint(client: TestClient) -> None:
    client.post("/auth/register", json=register_payload())
    token = login(client, "candidate@duvis.bo", "strong-password")

    response = client.get(
        "/auth/admin-only-test",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 403


def test_platform_admin_can_access_admin_only_endpoint(
    client: TestClient,
    platform_admin: User,
) -> None:
    token = login(client, platform_admin.email, "admin-password")

    response = client.get(
        "/auth/admin-only-test",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "role": "platform_admin"}


def test_public_registration_as_platform_admin_is_rejected(client: TestClient) -> None:
    response = client.post(
        "/auth/register",
        json=register_payload(
            email="new-admin@duvis.bo",
            role=UserRole.platform_admin.value,
        ),
    )

    assert response.status_code == 403
