from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Duvi's Job.bo API"
    app_version: str = "0.1.0"
    database_url: str = Field(
        default="postgresql+psycopg://duvis:duvis_password@localhost:5432/duvis_job_bo",
        alias="DATABASE_URL",
    )
    backend_cors_origins: list[str] = Field(
        default=["http://localhost:3000"],
        alias="BACKEND_CORS_ORIGINS",
    )
    secret_key: str = Field(
        default="change-me-in-local-development",
        alias="SECRET_KEY",
    )
    access_token_expire_minutes: int = Field(
        default=30,
        alias="ACCESS_TOKEN_EXPIRE_MINUTES",
    )
    algorithm: str = Field(default="HS256", alias="ALGORITHM")

    @field_validator("backend_cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, value: str | list[str]) -> list[str]:
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
