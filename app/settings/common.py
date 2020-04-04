import logging

APP_NAME = 'flask_setup_tut'
LOGGER_NAME = APP_NAME
DEBUG = False
TESTING = False
PROPAGATE_EXCEPTIONS = True
LOGGING_LEVEL = logging.INFO
SWAGGER = {
    "swagger_version": "2.0",
    "title": "Flasgger",
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
        ('Access-Control-Allow-Credentials', "true"),
    ],
    "specs": [
        {
            "version": "-1.0.1",
            "title": "Flask setup demo APIs",
            "endpoint": 'v1_flask_setup',
            "description": 'Flask Setup tutorial APIs',
            "route": '/v1/flask_setup'
        }
    ]
}
