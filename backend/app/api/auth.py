from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user, require_roles
from app.models.user import User, UserRole
from app.schemas.auth import LoginRequest, RegisterRequest, Token
from app.schemas.user import UserRead
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, db: Session = Depends(get_db)) -> User:
    return AuthService(db).register_user(
        email=payload.email,
        password=payload.password,
        full_name=payload.full_name,
        role=payload.role,
    )


@router.post("/login", response_model=Token)
def login(payload: LoginRequest, db: Session = Depends(get_db)) -> Token:
    auth_service = AuthService(db)
    user = auth_service.authenticate_user(email=payload.email, password=payload.password)
    access_token = auth_service.create_login_token(user)
    return Token(access_token=access_token)


@router.get("/me", response_model=UserRead)
def read_current_user(current_user: User = Depends(get_current_user)) -> User:
    return current_user


@router.get("/admin-only-test")
def admin_only_test(
    current_user: User = Depends(require_roles(UserRole.platform_admin)),
) -> dict[str, str]:
    return {"status": "ok", "role": current_user.role.value}
