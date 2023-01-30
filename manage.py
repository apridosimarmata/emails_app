from flask_script import Manager
from app import flask_app

manager = Manager(flask_app)

@manager.command
def runserver():
    flask_app.run()

@manager.command
def celery():
    celery -A app.celery worker --loglevel=info

@manager.command
def celery_beat():
    celery -A app.celery beat --loglevel=info

if __name__ == "__main__":
    manager.run()
