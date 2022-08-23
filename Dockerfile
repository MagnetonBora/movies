FROM python:3.10.6-slim-bullseye
WORKDIR /movies
COPY . /movies
RUN apt-get update && apt-get install -yq libpq-dev gcc
RUN pip install -r requirements.txt