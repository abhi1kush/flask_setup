from flask import request, jsonify
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from app.api.error import HTTPBadRequest
from app.service_error_codes import ServiceErrorCodes


class BaseAPIResource(Resource):
    error = ""

    def dispatch_request(self, *args, **kwargs):
        test_func = getattr(self, 'test_%s' % request.method.lower(), None)
        try:
            is_test_failed = test_func and not test_func(*args, **kwargs)
        except BadRequest as e:
            if e and hasattr(e, 'data'):
                raise HTTPBadRequest(
                    service_code=e.data.get(
                        'service_code', ServiceErrorCodes.KEY_PARSING_ERROR),
                    message=e.data.get('message')
                )
            raise HTTPBadRequest
        if is_test_failed:
            message = getattr(self, 'error', '')
            if message:
                raise HTTPBadRequest(message=message)
            raise HTTPBadRequest
        data = super(BaseAPIResource, self).dispatch_request(*args, **kwargs)
        if data.get("success") is None:
            data["success"] = True
        return jsonify(data)