from typing import Optional, Union

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=True)

    APP_ENV: str = "development"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "coffeeapp"
    TEST_DB_NAME: str = "test_db"
    SQLALCHEMY_DATABASE_URI: Optional[Union[PostgresDsn, str]] = None


settings = Settings()
