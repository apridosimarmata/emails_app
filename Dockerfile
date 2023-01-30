# syntax=docker/dockerfile:1

FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get install -y libpq-dev supervisor

# Install dependencies:
COPY . /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 4000

# Run the application:
COPY . .
CMD ["/usr/bin/supervisord", "-c", "/app/supervisord.conf"]
CMD celery -A app worker --loglevel=info --beat


