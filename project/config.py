import os
from pathlib import Path
from kombu import Queue


class BaseConfig:
    """Base configuration"""
    BASE_DIR = Path(__file__).parent.parent

    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3")

    CELERY_BROKER_URL = os.environ.get(
        "CELERY_BROKER_URL", "redis://127.0.0.1:6379/0")
    CELERY_RESULT_BACKEND = os.environ.get(
        "CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0")

    CELERY_TASK_DEFAULT_QUEUE = 'default'

    # Force all queues to be explicitly listed in `CELERY_TASK_QUEUES` to help prevent typos
    CELERY_TASK_CREATE_MISSING_QUEUES = False

    CELERY_TASK_QUEUES = (
        # need to define default queue here or exception would be raised
        Queue('default'),

        Queue('high_priority'),
        Queue('low_priority'),
    )

    SECRET_KEY = os.environ.get('SECRET_KEY')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

    SOCKETIO_MESSAGE_QUEUE = os.environ.get(
        'SOCKETIO_MESSAGE_QUEUE',
        'redis://127.0.0.1:6379/0'
    )

    CELERY_BEAT_SCHEDULE = {
        # Dynamic Config - similar process with one of these libs:
        # - redisbeat
        # - celery-sqlalchemy-scheduler

        # 'task-schedule-work': {
        #     'task': 'task_schedule_work',
        #     "schedule": 5.0,  # five seconds
        # },
    }


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
