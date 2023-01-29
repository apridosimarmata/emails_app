from flask import Blueprint

emails_api_prefix = 'api/emails'

emails_api = Blueprint(emails_api_prefix, __name__)

@emails_api.route("/save_emails", methods = ['POST'])
def api_save_emails():
    return 'ok'