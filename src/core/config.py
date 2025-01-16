from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseSettings):
    driver: str = "postgresql"
    user: str = "postgres"
    password: str = "postgres"
    host: str = "localhost"
    port: int = 5432
    db: str = "postgres"
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 30
    max_overflow: int = 10

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    def url(self, db_name: str | None = None) -> str:
        db_name = db_name or self.db
        return (
            "postgresql+asyncpg://"
            f"{self.user}:{self.password}@{self.host}:{self.port}/{db_name}"
        )


class CorsConfig(BaseSettings):
    allowed_hosts: str | list = ["*"]
    allowed_hosts_regex: str = ""
    allowed_credentials: bool = True
    allowed_methods: str = "*"
    allowed_headers: str | list = ["*"]

    @field_validator("allowed_hosts", mode="before", check_fields=False)
    @classmethod
    def split_allowed_hosts(cls, value):
        if isinstance(value, str):
            lst = value.split(",")
            return lst
        return value

    @property
    def get_list_allowed_methods(self) -> list[str]:
        return self.allowed_methods.split(",")

    @field_validator("allowed_headers", mode="before", check_fields=False)
    @classmethod
    def split_allowed_headers(cls, value):
        if isinstance(value, str):
            lst = value.split(",")
            return lst
        return value


class MainConfig(BaseSettings):
    debug: bool = False
    backend_host: str = "localhost"
    secret_key: str = "123"
    api_key: str = "secret"
    sentry_dsn: str = ""


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{Path(__file__).resolve().parent.parent.parent}/secrets/.envfile",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_ignore_empty=True,
        extra="ignore",
    )
    realm: str = "GEOSEARCH"
    app: MainConfig = MainConfig()
    postgres: DatabaseConfig = DatabaseConfig()
    cors: CorsConfig = CorsConfig()


config = Config()
