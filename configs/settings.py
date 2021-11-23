from typing import List
import secrets

from pydantic import BaseSettings, AnyHttpUrl

class Settings(BaseSettings):

    PROJECT_NAME = "Default"
    SECRET_KEY = secrets.token_urlsafe(32)
    
    # Versioning
    API_DEFAULT: str = "/api"

    # CORS Configs
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_DATABASE_URI: str



settings = Settings()