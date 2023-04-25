FROM python:3.11
RUN mkdir /etl
WORKDIR /etl
COPY ./requirements.txt requirements.txt
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
RUN apt-get update && apt-get install -y netcat
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/etl/entrypoint.sh"]