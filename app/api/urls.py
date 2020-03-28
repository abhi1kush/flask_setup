from app import api, flask_setup_ns
from app.api.views import HealthCheckAPIView, RedisDemoAPIView, AddAPIView

flask_setup_ns.add_resource(HealthCheckAPIView, '/flask_setup/healthcheck')
flask_setup_ns.add_resource(RedisDemoAPIView, '/flask_setup/redis')
flask_setup_ns.add_resource(AddAPIView, '/flask_setup/add')
