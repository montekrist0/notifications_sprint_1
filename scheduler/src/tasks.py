from celery import Celery
from celery.schedules import crontab
from core.settings import broker_url, settings
from db_manager import MongoDatabaseManager
from pymongo import MongoClient

from scheduler import Scheduler

app = Celery("tasks", broker=broker_url)
app.conf.task_queues = {"periodic": {"exchange": "periodic"}}

mongo_client = MongoClient(host=settings.mongo_host, port=settings.mongo_port)
db_manager = MongoDatabaseManager(mongo_client)
scheduler = Scheduler(db_manager=db_manager)


@app.task
def generate_reviews_like_events():
    scheduler.get_review_like_event()


@app.task
def generate_top_week_viewed_movie_event():
    scheduler.get_week_top_viewed_movie_event()


@app.task
def generate_new_movie_event():
    scheduler.get_personal_selections()


app.conf.beat_schedule = {
    "review_like_event": {
        "task": "tasks.generate_reviews_like_events",
        "schedule": crontab(hour=12, minute=0),
        "options": {"queue": "periodic"},
    },
    "top_week_viewed_movie_event": {
        "task": "tasks.generate_top_week_viewed_movie_event",
        "schedule": crontab(hour=12, minute=0, day_of_week=1),
        "options": {"queue": "periodic"},
    },
    "new_movie_event": {
        "task": "tasks.generate_new_movie_event",
        "schedule": crontab(hour=13, minute=0),
        "options": {"queue": "periodic"},
    },
}
