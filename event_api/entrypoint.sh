#!/bin/sh

gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8001 --access-logfile - --access-logformat '{"timestamp": "%(asctime)s", "severity": "%(levelname)s", "module": "%(module)s", "message": "%(message)s"}' --log-level INFO