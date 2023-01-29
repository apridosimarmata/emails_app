from flask import Blueprint, request
from controller.emails import *
emails_api_prefix = 'api/emails'

emails_api = Blueprint(emails_api_prefix, __name__)

@emails_api.route("/save_emails", methods = ['POST'])
def api_save_emails():
    data = request.json
    return save_email(data)