from celery import Celery
from celery.schedules import crontab
from core.settings import broker_url
from db_manager import MongoDatabaseManager

from scheduler import Scheduler

app = Celery("tasks", broker=broker_url)

db_manager = MongoDatabaseManager()
scheduler = Scheduler(db_manager=db_manager)


@app.task(queue="reviews_like")
def generate_reviews_like_events():
    scheduler.get_review_like_event()


@app.task(queue="top_week_movie")
def generate_top_week_viewed_movie_event():
    scheduler.get_week_top_viewed_movie_event()


@app.task(queue="new_movie")
def generate_new_movie_event():
    scheduler.get_new_film_event()


app.conf.beat_schedule = {
    "review_like_event": {
        "task": "generate_reviews_like_events",
        "schedule": crontab(hour=12, minute=0),
    },
    "top_week_viewed_movie_event": {
        "task": "generate_top_week_viewed_movie_event",
        "schedule": crontab(hour=12, minute=0, day_of_week=1),
    },
    "new_movie_event": {
        "task": "generate_new_movie_event",
        "schedule": crontab(hour=12, minute=0, day_of_week=1),
    },
}
