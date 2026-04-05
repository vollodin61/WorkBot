from telethon import client, events

from src.config.conf import BotConfig


@client.on(events.NewMessage(chats=BotConfig.work_bot_chat_id))
async def handle_contacts(event: events.NewMessage.Event) -> None:
    await event.reply("Получил контакты")
