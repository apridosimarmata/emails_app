# syntax=docker/dockerfile:1

FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get install -y libpq-dev

# Install dependencies:
COPY . /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 4000

# Run the application:
COPY . .
CMD ["nohup", "python3", "main.py"]
CMD ["celery", "-A", "app", "worker", "--loglevel=info", "--beat"]
