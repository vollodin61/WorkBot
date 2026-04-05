from src.config.conf import BotConfig, info_logger, error_logger


async def start_message():
    async with BotConfig.tele_ubot:
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
