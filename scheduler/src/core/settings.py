from enum import Enum

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    rabbitmq_host: str = Field(default="localhost")
    rabbitmq_port: int = Field(default=5672)
    rabbitmq_username: str = Field(default="admin")
    rabbitmq_password: str = Field(default="admin")

    mongo_host: str = Field(env="WORKER_MONGO_HOST", default="localhost")
    mongo_port: int = Field(env="WORKER_MONGO_PORT", default=27127)
    mongo_db: str = Field(env="worker_mongo_db", default="notifications")
    mongo_collection_notifications: str = Field(
        env="worker_mongo_collection_notifications", default="notifications"
    )

    event_api_base_url: str
    event_api_like_url: str
    event_api_personal_selection_url: str
    event_api_mass_notifications_url: str


class ApiSettings(str, Enum):
    pass


settings = Settings()
broker_url = (
    f"pyamqp://{settings.rabbitmq_username}:{settings.rabbitmq_password}@{settings.rabbitmq_host}:"
    f"{settings.rabbitmq_port}/"
)
