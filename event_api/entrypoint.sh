#!/bin/sh

gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8001