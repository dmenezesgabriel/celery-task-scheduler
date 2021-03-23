import os
import platform


class Config(object):
    MACHINE_NAME = os.getenv("MACHINE_NAME")

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Application
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    LOG_TO_STDOUT = os.getenv("LOG_TO_STDOUT")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///" + os.path.join(BASE_DIR, "app.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Celery
    CELERY_BROKER_URL = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND = "redis://redis:6379/0"
    CELERY_ACCEPT_CONTENT = ["application/json"]
    CELERY_RESULT_SERIALIZER = "json"
    CELERY_TASK_SERIALIZER = "json"
    CELERY_TIMEZONE = "America/Sao_Paulo"
    CELERY_BEAT_SCHEDULE = {}

    # Redis
    REDIS_HOST = "localhost"
    REDIS_PASSWORD = ""
    REDIS_PORT = 6379
    REDIS_URL = "redis://redis:6379/0"
    # Messages
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_DEFAULT_CHAT_ID = os.getenv("TELEGRAM_DEFAULT_CHAT_ID")
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    SLACK_DEFAULT_CHANNEL = os.getenv("SLACK_DEFAULT_CHANNEL")


class DevelopmentConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"


class ProductionConfig(Config):
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    # Redis:
    REDIS_URL = os.environ.get("REDIS_URL")
    CELERY_BROKER_URL = os.environ.get("REDIS_URL")
    CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL")
