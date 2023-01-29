from flask import Blueprint

emails_page_prefix = 'emails'

emails_page = Blueprint(emails_page_prefix, __name__)

@emails_page.route("", methods = ['GET'])
def page_email():
    return 'ok'