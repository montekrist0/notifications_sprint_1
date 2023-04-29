import requests


from config.celery import app


@app.task(acks_late=True)
def send_event(url_event: str, body_request: dict):
    requests.post(url_event, json=body_request)
