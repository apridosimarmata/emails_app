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

```docker run --name email_app -d -p 4000:4000 --network email_app jublia``` starting app
```docker run --name email_app_db -d -p 5432:5432 --network email_app postgres``` starting db
Creating database
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
```

```docker run --name email_app_redis -d -p 6379:6379 --network email_app redis``` starting redis


## Database

```docker run --name email_app_db -e POSTGRES_PASSWORD=email_app POSTGRES_USER=postgres -d -p 5432:5432 --network email_app postgres```

```python3 app.py```

```celery -A app worker --loglevel=info --beat```


```curl -H "Content-Type: application/json" -X POST -d '{ "event_id": 1, "email_subject": "Important Meeting", "email_content": "PayDay sale! Checkout now at this link", "timestamp": "2023-02-01T09:00:00Z" }' http://localhost:4001/api/emails/save_emails```