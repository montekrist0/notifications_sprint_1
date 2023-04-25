#!/bin/sh
echo "Waiting for auth service..."

    while ! nc -z $ETL_AUTH_HOST $ETL_AUTH_PORT; do
      sleep 0.1
    done

    echo "Auth available"


echo "Waiting for mongo..."

    while ! nc -z $ETL_MONGO_HOST $ETL_MONGO_PORT; do
      sleep 0.1
    done

    echo "Mongo available"

python3 main.py
exec "$@"