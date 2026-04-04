from telethon import client, events

from src.config.conf import BotConfig


@client.on(events.NewMessage(chats=BotConfig.MY_CHAT_ID))
async def handle_contacts(event: events.NewMessage.Event) -> None:
    await event.reply("Получил контакты")
