#!/usr/bin/env bash
cd /opt/app

python manage.py collectstatic --no-input --clear

while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
done

python manage.py migrate

set -e

chown www-data:www-data /var/log

uwsgi --strict --ini /opt/app/uwsgi.ini
