from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import create_access_token, get_password_hash, verify_password
from app.models.user import User, UserRole
from app.repositories.user_repository import UserRepository

PUBLIC_REGISTRATION_ROLES = {
    UserRole.candidate,
    UserRole.company_user,
    UserRole.company_admin,
}


class AuthService:
    def __init__(self, db: Session) -> None:
        self.user_repository = UserRepository(db)

    def register_user(
        self,
        *,
        email: str,
        password: str,
        full_name: str,
        role: UserRole,
    ) -> User:
        if role not in PUBLIC_REGISTRATION_ROLES:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="This role cannot be registered publicly.",
            )

        if self.user_repository.get_by_email(email) is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A user with this email already exists.",
            )

        try:
            return self.user_repository.create(
                email=email,
                hashed_password=get_password_hash(password),
                full_name=full_name,
                role=role,
            )
        except IntegrityError as exc:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A user with this email already exists.",
            ) from exc

    def authenticate_user(self, *, email: str, password: str) -> User:
        user = self.user_repository.get_by_email(email)
        if user is None or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive.",
            )

        return user

    def create_login_token(self, user: User) -> str:
        return create_access_token(subject=str(user.id))
