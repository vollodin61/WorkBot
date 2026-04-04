import asyncio
import os
import sys

from src.config.conf import BotConfig  # todo странно, что тут подчеркивает BotConfig


sys.path.insert(1, os.path.join(sys.path[0], '..'))


async def start_message():
    async with BotConfig.tele_ubot:
        await BotConfig.tele_ubot.send_message(
            entity="me",
            message="Бот MinZKH запущен"
        )


async def main():
    await start_message()
    BotConfig.scheduler.start()
    await asyncio.Event().wait()


if __name__ == '__main__':
    asyncio.run(main())
