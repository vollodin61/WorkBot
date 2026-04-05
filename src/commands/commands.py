from aiogram import Bot
from aiogram.types import (
    BotCommand,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeChat,
)

from src.config.conf import BotConfig


async def set_commands(bot: Bot):
    await bot.set_my_commands(
        [
            BotCommand(command='start', description='Стартуем, админ!'),  # todo команды запилить
    #         BotCommand(command='cancel', description='Сбросить последнее действие'),
    #         BotCommand(command='add_to_excluded', description='Добавить чат в игнор'),
    #         BotCommand(command="add_reminder", description="Поставить напоминание"),
    #         BotCommand(command="rm_reminder", description="Отменить напоминание"),
    #         BotCommand(command='reminders_to_chat', description="Поставить напоминалки для всех в чате"),
    #         BotCommand(command='rm_reminder_to_chat', description="Удалить напоминалки для всех в чате"),
    #         BotCommand(command='rm_non_cat_participants', description="Удалить безкошатников"),
    #         BotCommand(command='rm_chat_from_excluded', description="Удалить чат из исключений"),
    #         BotCommand(command='send_msg_to_all', description="Отправить сообщение всем"),
    #     ],
    #     scope=BotCommandScopeChat(chat_id=BotConfig.admins_ids[0])
    # )
    # await bot.set_my_commands(
    #     [
    #         BotCommand(command="start", description="Стартуем! Сегодня мы с тобой стартуем! 😁"),
    #         BotCommand(command="add_reminder", description="Поставить напоминание"),
    #         BotCommand(command="rm_reminder", description="Отменить напоминание"),
    #         BotCommand(command="help", description="Помощь"),
    #         BotCommand(command="site", description="Перейти на сайт fillatova.ru"),
        ],
        scope=BotCommandScopeAllPrivateChats()  # уровни доступа тоже запилить
    )
