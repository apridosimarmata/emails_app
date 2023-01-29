from flask import Flask
app = Flask(__name__)

from interface.views.emails import emails_page, emails_page_prefix
from interface.api.emails import emails_api, emails_api_prefix

app.register_blueprint(emails_page, url_prefix = f"/{emails_page_prefix}")
app.register_blueprint(emails_api, url_prefix = f"/{emails_api_prefix}")

print(app.url_map)
