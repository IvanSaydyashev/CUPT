from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

class Settings(BaseSettings):
    load_dotenv()

    POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'user')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD', 'admin')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB', 'cupt_db')
    POSTGRES_PORT: int = int(os.getenv('POSTGRES_PORT', 5432))
    POSTGRES_HOST: str = os.getenv('POSTGRES_HOST', 'localhost')

    DATABASE_URL: str = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    BOT_TOKEN: str = os.getenv('BOT_TOKEN', '')

settings = Settings()