from data.request import SaveEmailRequest
from utils.response import make_response
import http

def save_email(data):
    save_email_data = SaveEmailRequest(
        data.get('event_id'),
        data.get('email_subject'),
        data.get('email_content'),
        data.get('timestamp')
    )

    

    return make_response(
        http.HTTPStatus.OK,
        "Email disimpan",
        None
    )