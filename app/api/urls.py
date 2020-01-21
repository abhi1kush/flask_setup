from app import api
from app.api.views import HealthCheckAPIView

api.add_resource(HealthCheckAPIView, '/flask_setup/healthcheck')
