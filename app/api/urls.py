from app import api
from app.api.views import HealthCheckAPIView, RedisDemoAPIView

api.add_resource(HealthCheckAPIView, '/flask_setup/healthcheck')
api.add_resource(RedisDemoAPIView, '/flask_setup/redis')