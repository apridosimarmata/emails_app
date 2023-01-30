from app import flask_app


from interface.views.emails import emails_page, emails_page_prefix
from interface.api.emails import emails_api, emails_api_prefix

flask_app.register_blueprint(emails_page, url_prefix = f"/{emails_page_prefix}")
flask_app.register_blueprint(emails_api, url_prefix = f"/{emails_api_prefix}")

if __name__ == "__main__":
    flask_app.run(host = "0.0.0.0", port = "4001")