from flask_rq2 import RQ
from flask import Flask
from flask_restplus import Api, fields
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
api = Api(app, version=1.0, title='Flask Setup Demo', description='Flask Setup APIs for reference.')
redis_q = RQ(app)
Swagger(app=app)


flask_setup_ns = api.namespace(
    'Flask Setup Demo APIs',
    description='Various APIs with basic functionality for future reference.'
)


__import__('app.api')

