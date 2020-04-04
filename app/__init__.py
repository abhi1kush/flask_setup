from flask_rq2 import RQ
from flask import Flask
from flask_restful import Api
from app import settings
import rq_dashboard
from flasgger import Swagger

class BaseRestApiException(Exception):
    pass


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.name = app.config["APP_NAME"]
    return app


app = create_app()
app.url_map.strict_slashes = False
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/math-ocr/rq")
api = Api(app)
redis_q = RQ(app)
swagger = Swagger(app)

__import__('app.api')

