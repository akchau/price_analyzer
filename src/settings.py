import os
from pathlib import Path

from pydantic import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    PRICE_DIR: str

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')


settings = Settings()
