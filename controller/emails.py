from data.emails import Emails, EventRegistration, People
from utils.response import make_response
from utils.date import string_to_timestamp, get_now
from data.database import db
import http

def save_email(data):
    save_email_data = Emails(
        event_id = data.get('event_id'),
        email_subject = data.get('email_subject'),
        email_content = data.get('email_content'),
        timestamp = string_to_timestamp(data.get('timestamp'))
    )

    db.session.add(save_email_data)
    db.session.commit()
    db.session.close()
    
    return make_response(
        http.HTTPStatus.OK,
        "Email disimpan",
        None
    )

def get_current_minute_email():
    return db.session.query(Emails).filter(Emails.timestamp == get_now()).all()

def get_recipients_by_event_id(event_id):
    recipients = []
    for registration in db.session.query(EventRegistration).filter(EventRegistration.event_id == event_id).all():
        recipients.append(
            db.session.query(People).filter(People.id == registration.people_id).first()
        )
    return recipients

