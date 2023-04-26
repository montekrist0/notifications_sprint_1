from celery import Celery
from config import broker_url

app = Celery("tasks", broker=broker_url)


@app.task(queue="tasks")
def add(x, y):
    return x + y


a = add.apply_async((2, 2))
