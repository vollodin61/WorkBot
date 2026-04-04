from telethon import client, events


@client.on(events.NewMessage(chats=MY_CHAT_ID))
async def handle_contacts(event: events.NewMessage.Event) -> None:
    await event.reply("Получил контакты")
