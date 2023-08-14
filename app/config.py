from pydantic_settings import BaseSettings
from typing import Set


class AppConfig(BaseSettings):
    allowed_origins: Set[str]
    jwt_secret_key: str
    mongo_uri: str
    db_name: str