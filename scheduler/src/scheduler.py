from enum import Enum

import requests
from core.settings import settings
from db_manager import MongoDatabaseManager
from fake_services.film_service import FakeMovieService


class Groups(Enum):
    subscribers = 1
    users = 2
    editors = 3
    admins = 4

    def __str__(self):
        return str(self.value)


class Scheduler:
    def __init__(self, db_manager: MongoDatabaseManager):
        self.db_manager = db_manager
        self.movie_service = FakeMovieService()

    def get_review_like_event(self):
        if events := self.db_manager.get_review_like_persons_for_notification():
            for event in events:
                requests.post(url=settings.event_api_like_url, json=event)

    def get_week_top_viewed_movie_event(self):
        top_movie = self.movie_service.get_top_week_viewed_movies()
        event_payload = {'group_id': str(Groups.subscribers), 'content': top_movie}
        requests.post(url=settings.event_api_mass_notifications_url, json=event_payload)

    def get_personal_selections(self):
        pass
