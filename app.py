from flask import Flask
from flask_script import Manager


''' SETTING UP FLASK APP '''
flask_app = Flask(__name__)


''' SETTING UP CELERY '''

from celery import Celery
from datetime import timedelta

flask_app.config.update(CELERY_CONFIG={
    'broker_url': 'redis://localhost:6379',
    'result_backend': 'redis://localhost:6379',

})

def make_celery(app):
    celery = Celery(app.import_name)
    celery.conf.update(app.config["CELERY_CONFIG"])
    celery.conf.beat_schedule = {
        'send_email': {
            'task': 'app.send_email',
            'schedule': timedelta(seconds=1),
        }
    }

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery_app = make_celery(flask_app)

from controller.emails import get_current_minute_email
from utils.email import send_email as send
@celery_app.task
def send_email():
    emails = get_current_minute_email()
    for email in emails:
        send_email()
    # Send the email
    # ...



