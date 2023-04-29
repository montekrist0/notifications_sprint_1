#!/bin/sh

python3 main.py &
celery -A tasks worker -Q tasks -E -n worker1@%h --concurrency=1
