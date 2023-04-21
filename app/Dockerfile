FROM python:3.10

WORKDIR /opt/app
#COPY entrypoint.sh entrypoint.sh

RUN apt -y update \
    && apt -y install netcat

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

COPY run_uwsgi.sh run_uwsgi.sh
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini

RUN mkdir -p /opt/app/static/ \
     && mkdir -p /opt/app/media/ \
     && pip install --upgrade pip \
     && pip install -r requirements.txt

EXPOSE 8000
COPY . .
RUN chmod 777 /opt/app/static/ && chmod 777 /opt/app/media/
RUN chmod 777 /opt/app/run_uwsgi.sh
#ENTRYPOINT ["/opt/app/entrypoint.sh"]
