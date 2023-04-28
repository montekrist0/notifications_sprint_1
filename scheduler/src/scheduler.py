from typing import List

from db_manager import MongoDatabaseManager


class Scheduler:
    def __init__(self, db_manager: MongoDatabaseManager):
        pass

    def get_review_like_event(self) -> List[dict]:
        pass

    def get_new_film_event(self):
        pass

    def get_week_top_viewed_movie_event(self):
        pass
