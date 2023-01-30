# Email app

Save an email for later being sent to recipients for any specified time.

There are three instance in this system:

1. The app (Python, Flask)
2. Redis (as broker)
3. Database (as app's data storage)

### How to set up


```docker pull postgres```

```docker pull redis```

## Creating a network

```docker network create email_app```

## Starting the containers

```docker run --name email_app_db -e POSTGRES_PASSWORD=email_app POSTGRES_USER=postgres -d -p 5432:5432 --network email_app postgres``` starting db

```docker run --name email_app_redis -d -p 6379:6379 --network email_app redis``` starting redis


## Setting up database
```docker exec -it email_app_db bash```

```psql -U postgres``

```CREATE DATABASE email_app;```

```\c email_app;```

```
CREATE TABLE emails (
  id SERIAL PRIMARY KEY,
  event_id INTEGER,
  email_subject VARCHAR(255),
  email_content TEXT,
  timestamp TIMESTAMP
);

CREATE TABLE people (
    id serial PRIMARY KEY,
    name VARCHAR(255),
    email_address VARCHAR(255)
);

CREATE TABLE event (
    id serial PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE event_registration (
    people_id INTEGER PRIMARY KEY,
    event_id INTEGER,
    FOREIGN KEY (people_id) REFERENCES people (id),
    FOREIGN KEY (event_id) REFERENCES event (id)
);

INSERT INTO people (name, email_address) VALUES ('Rudi', 'rudi@example.com');
INSERT INTO people (name, email_address) VALUES ('Andi', 'andi@example.com');
INSERT INTO people (name, email_address) VALUES ('Siti', 'siti@example.com');

INSERT INTO event (name) VALUES ('Seminar Web Development');
INSERT INTO event (name) VALUES ('Workshop Mobile Development');

INSERT INTO event_registration (people_id, event_id) VALUES (1, 1);
INSERT INTO event_registration (people_id, event_id) VALUES (2, 2);
INSERT INTO event_registration (people_id, event_id) VALUES (3, 1);

```



## Setting up app
```docker build --tag jublia .``` build image

```docker run --name email_app -d -p 4000:4000 --network email_app jublia``` starting app




## Send an email data
```curl -H "Content-Type: application/json" -X POST -d '{ "event_id": 1, "email_subject": "Payday Sale!", "email_content": "PayDay sale! Checkout now at this link", "timestamp": "30 Jan 2023 16:11" }' http://localhost:4001/api/emails/save_emails```