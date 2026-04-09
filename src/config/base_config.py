import logging
from typing import Any

from environs import Env
from loguru import logger
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_fixed


env = Env()
env.read_env()

info_logger = logger.info
error_logger = logger.error
warning_logger = logger.warning
exception_logger = logger.exception
debug_logger = logger.debug

logging.basicConfig(level=logging.INFO)


class BaseConfig:
    TIMEOUT = 4
    RETRY = 4

    @staticmethod
    def log_action(service_name: str = None, action: Any = None):
        if service_name.endswith("_bot"):
            log_file = f"src/logs/{service_name}.log"
        else:
            log_file = f"logs/{service_name}.log"
        service_logger = logging.getLogger(f"service_{service_name}")
        service_logger.setLevel(logging.INFO)
        if not service_logger.handlers:
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            service_logger.addHandler(file_handler)

        service_logger.info(action)

    @staticmethod
    def log_retry_attempt(retry_state):
        exception = retry_state.outcome.exception()
        BaseConfig.log_action(
            service_name=retry_state.fn.__qualname__, action=exception
        )

    @staticmethod
    def log_final_exception(retry_state):
        exception = retry_state.outcome.exception()
        BaseConfig.log_action(
            service_name=retry_state.fn.__qualname__, action=exception
        )

    base_retry = retry(
        stop=stop_after_attempt(RETRY),
        wait=wait_fixed(TIMEOUT),
        retry=retry_if_exception_type(Exception),
        after=log_retry_attempt,
        retry_error_callback=log_final_exception,
    )

