import asyncio

from src.config.base_config import info_logger, error_logger
from src.config.bot_config import BotConfig


info_logger("ffпытаюсь отправить сообщение")


async def start_message():
    async with BotConfig.tele_ubot:
        info_logger("aaпытаюсь отправить сообщение")
        try:
            await BotConfig.tele_ubot.send_message(
                entity="me",
                message="Бот MinZKH запущен"
            )
            info_logger(f"Юзербот отправил сообщение")
            await BotConfig.tele_ubot.send_message(
                entity=-1005275643764,
                message="Бот MinZKH запущен"
            )
        except Exception as e:
            error_logger(f"Юзербот не включен!! ОШИБКА!! {repr(e)}")


asyncio.run(start_message())
