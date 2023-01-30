from flask import Flask


''' SETTING UP FLASK APP '''
flask_app = Flask(__name__)


''' SETTING UP CELERY '''

from celery import Celery
from datetime import timedelta

# Could be env vars, configured for docker. You may change host to localhost

flask_app.config.update(CELERY_CONFIG={
    'broker_url': 'redis://email_app_redis:6379',
    'result_backend': 'redis://email_app_redis:6379',

})

def make_celery(app):
    celery = Celery(app.import_name)
    celery.conf.update(app.config["CELERY_CONFIG"])
    celery.conf.beat_schedule = {
        'send_email': {
            'task': 'app.send_email',
            'schedule': timedelta(minutes=1),
        }
    }

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery_app = make_celery(flask_app)

from controller.emails import get_current_minute_email, get_recipients_by_event_id
from utils.email import send_email as send
@celery_app.task
def send_email():
    emails = get_current_minute_email()
    for email in emails:
        event_id = email.event_id
        recipients = get_recipients_by_event_id(event_id)
        for recipient in recipients:
            send(recipient.email_address, email.email_subject, email.email_content)



