import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseSettings


DEBUG = True
if DEBUG:
    env_path = Path('.') / '.env.local'
    load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    AUTH_HOST_PORT: str = f"""{os.getenv('ETL_AUTH_HOST')}:{os.getenv('ETL_AUTH_PORT')}"""
    USERINFO_ENDPOINT: str = os.getenv('ETL_ENDPOINT_URL')

    MONGO_HOST: str = os.getenv('ETL_MONGO_HOST')
    MONGO_PORT: int = int(os.getenv('ETL_MONGO_PORT'))
    DB_NAME: str = os.getenv('ETL_MONGO_DBNAME')
    COLLECTION: str = os.getenv('ETl_MONGO_COLLECTION')

    SLEEP: int = os.getenv('ETL_INTERVAL')
    BATCH_SIZE: int = os.getenv('ETL_BATCH_SIZE')
