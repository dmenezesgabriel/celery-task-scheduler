import logging
import os
from logging.handlers import RotatingFileHandler

from config import Config
from flask import Flask
from tasks import *

from src.api.routes import bp as api_bp
from src.extensions import celery


def init_celery(celery, app):
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask


def create_app(config_class=Config):
    """
    Application Factory funcion which makes possibleto instantiate different
    app environments

    Returns
    ----------------
    Flask app object
    """
    # Create and configure the app

    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(api_bp)

    init_celery(celery, app)

    # Logging config
    if not app.testing:
        if app.config["LOG_TO_STDOUT"]:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists("logs"):
                os.mkdir("logs")
            file_handler = RotatingFileHandler(
                "logs/flask-notes.log", maxBytes=10240, backupCount=10
            )
            file_handler.setFormatter(
                logging.Formatter(
                    """%(asctime)s %(levelname)s: %(message)s """
                    """[in %(pathname)s:%(lineno)d]"""
                )
            )
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

            app.logger.setLevel(logging.INFO)
            app.logger.info("Flask Notes startup")

    return app
