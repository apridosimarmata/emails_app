# syntax=docker/dockerfile:1

FROM python:3.9-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN sudo apt-get install libpq-dev

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 4000

# Run the application:
COPY . .
CMD ["python", "app.py"]