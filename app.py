from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h2>'

from interface.views.emails import emails_page, emails_page_prefix
from interface.api.emails import emails_api, emails_api_prefix

app.register_blueprint(emails_page, url_prefix = f"/{emails_page_prefix}")
app.register_blueprint(emails_api, url_prefix = f"/{emails_api_prefix}")

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port = 4001)