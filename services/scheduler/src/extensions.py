from celery import Celery
from config import Config


celery = Celery(
    __name__,
    backend=Config.CELERY_RESULT_BACKEND,
    broker=Config.CELERY_BROKER_URL
)
