from redis.asyncio.client import Redis
from redis.backoff import ExponentialBackoff
from redis.exceptions import BusyLoadingError, ConnectionError, TimeoutError
from redis.retry import Retry

from src.config.base_config import BaseConfig, env, info_logger


class RedisConfig(BaseConfig):
    redis_instance = None
    RETRY = 3
    TIMEOUT = 3

    @staticmethod
    @BaseConfig.base_retry
    def get_connection():
        redis_host = env("REDIS_HOST")
        # redis_host = "localhost"
        redis_port = env("REDIS_PORT")
        if not RedisConfig.redis_instance:
            RedisConfig.redis_instance = Redis(
                host=redis_host,
                port=int(redis_port),
                socket_timeout=RedisConfig.TIMEOUT,
                retry=Retry(ExponentialBackoff(), RedisConfig.RETRY),
                retry_on_error=[BusyLoadingError, ConnectionError, TimeoutError],
            )
            info_logger("Redis подключён")

        return RedisConfig.redis_instance
