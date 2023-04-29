"""Модуль, описывающий менеджера по работе с базой данных уведомлений."""
from typing import List

from core.settings import settings
from pydantic import BaseModel
from pymongo import MongoClient


class ReviewLikeModel(BaseModel):
    user_id: str
    review_id: str


class MongoDatabaseManager:
    """Менеджер базы данных уведомлений."""

    def __init__(self, mongo_client: MongoClient):
        self.mongo_client = mongo_client
        self.notification_db = self.mongo_client.get_database(settings.mongo_db)
        self.notification_collection = self.notification_db.get_collection(
            settings.mongo_collection_notifications
        )

    def get_review_like_persons_for_notification(self) -> List[dict]:
        """Метод для поиска тех, кому уже можно отправить письмо."""

        query = {"content.review_id": {"$exists": True}}
        review_notifications = list(
            filter(
                lambda doc: doc["content"]["likes_count_new"]
                > doc["content"]["likes_count_old"],
                self.notification_collection.find(query),
            )
        )

        return [
            ReviewLikeModel(**notif.get("content")).dict()
            for notif in review_notifications
        ]
