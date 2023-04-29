#!/bin/sh

celery -A tasks worker -Q periodic &
celery -A tasks beat
