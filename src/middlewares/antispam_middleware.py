from asyncio import sleep as asy_sleep
from random import randint
from typing import Dict, Any, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.types import Message
from aiogram.types.base import TelegramObject

from src.config.base_config import debug_logger
from src.config.bot_config import BotConfig


class Antispam(BaseMiddleware):

    def __init__(self, storage: RedisStorage):
        self._storage = storage

    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]],
                       Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]) -> Any:
        # Пропускаем админов и самого бота
        if event.from_user.id in BotConfig.admins_ids or event.from_user.id == BotConfig.bot.id:
            return await handler(event, data)

        # Ключ для хранения количества запросов пользователя
        user_key = f"user{event.from_user.id}"

        # Получаем текущее количество запросов
        request_count = await self._storage.redis.get(name=user_key)
        debug_logger(request_count)

        if request_count:
            if request_count.decode().isdigit():
                request_count = int(request_count.decode())
                if request_count >= 4:  # Лимит запросов
                    wait = randint(11, 16)  # Случайное время ожидания
                    await self._storage.redis.set(name=user_key, value='block', ex=wait)
                    await event.answer(text=f"Помедленнее, я записую... Подождите {wait} секунд",
                                       reply_to_message_id=event.message_id)
                    await asy_sleep(wait)
                    await event.answer(text="Пишите, но не торопясь, я ж записую ✍️👀")
                    return  # Прекращаем обработку сообщения
                else:
                    request_count += 1
                    await self._storage.redis.set(name=user_key, value=request_count, ex=10 - request_count * 2)
            else:
                return
        else:
            await self._storage.redis.set(name=user_key, value=1, ex=10)
        return await handler(event, data)
