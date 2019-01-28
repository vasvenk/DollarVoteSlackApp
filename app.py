from flask import Flask

import requests
import os


app = Flask(__name__)

clientSecret = os.environ.get('ClientSecret')
clientId = os.environ.get('ClientID')
webhookUrl = os.environ.get('WebhookURL')

@app.route("/")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
