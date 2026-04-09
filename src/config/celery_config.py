from celery import Celery

from src.config.base_config import BaseConfig, env, info_logger


class CeleryConfig(BaseConfig):
    CELERY_BROKER_URL: str = env("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND: str = env("CELERY_RESULT_BACKEND")
    _instance = None

    @staticmethod
    @BaseConfig.base_retry
    def get_celery_client():
        if not CeleryConfig._instance:
            CeleryConfig._instance = Celery(
                broker=CeleryConfig.CELERY_BROKER_URL,
                backend=CeleryConfig.CELERY_RESULT_BACKEND,
            )
            info_logger("Celery инициализирован")

        return CeleryConfig._instance
