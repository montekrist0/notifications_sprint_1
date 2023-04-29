"""Модуль, предназначенный для имитации общения с сервисом фильмов и получения новинок"""
from faker import Faker


class FakeMovieService:
    """Класс, имитирующий работу с сервисом фильмов и аналитической платформой, для выдачи рекомендаций."""

    def __init__(self):
        self.faker = Faker()

    def get_top_week_viewed_movies(self):
        """Метод возвращает самые популярные фильмы за неделю"""
        movie_name = f"{self.faker.catch_phrase()} {self.faker.word()}"
        return f"Hey, there! On last week {movie_name} was in top views!"

    def get_recommendations_for_users(self):
        """Метод должен возвращать рекомендации по всем пользователям"""
        pass
