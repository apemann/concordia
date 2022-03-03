FROM python:3.8-alpine

WORKDIR /app

ADD . /app

RUN apk update && apk add gcc musl-dev libffi-dev g++ postgresql-dev && pip install -r requirements.txt

# Start Gunicorn with 3 workers
CMD gunicorn -b 0.0.0.0:8080 -w 3 run:app