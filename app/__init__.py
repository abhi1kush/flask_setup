from flask import Flask
from flask_restful import Api
# import sentry_sdk
# from sentry_sdk.integration.flask import FlaskIntegration
from elasticsearch_dsl import connections

from app import settings
from werkzeug.exceptions import HTTPException


class BaseRestApiException(Exception):
    pass


def create_es_connection():
    connection = connections.create_connection(hosts=settings.ES_CLUSTER_CONFIG, timeout=60)
    return connection


def create_app():
    # sentry_sdk.init(
    #     dsn=settings.SENTRY_DSN,
    #     ignore_errors=[HTTPException, BaseRestApiException],
    #     integrations=[FlaskIntegration()],
    #     enviornment=settings.ENV
    # )
    app = Flask(__name__)
    app.config.from_object(settings)
    app.name = app.config["APP_NAME"]
    return app


app = create_app()
es = create_es_connection()
api = Api(app)

__import__('app.api')
