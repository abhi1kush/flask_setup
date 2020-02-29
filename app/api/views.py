from app.api.base import BaseAPIResource


class HealthCheckAPIView(BaseAPIResource):
    def get(self):
        return {
                "status": "success",
                "version": 0.1
        }


