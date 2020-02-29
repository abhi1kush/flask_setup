from flask import Flask
from flask_restful import Api
from app import settings


class BaseRestApiException(Exception):
    pass


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.name = app.config["APP_NAME"]
    return app


app = create_app()
api = Api(app)

__import__('app.api')

