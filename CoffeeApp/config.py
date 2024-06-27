from typing import Optional, Union

from pydantic import PostgresDsn
from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    APP_ENV: str = "development"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "coffeeapp"
    TEST_DB_NAME: str = "coffeeapp_test"
    SQLALCHEMY_DATABASE_URI: Optional[Union[PostgresDsn, str]] = None

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
