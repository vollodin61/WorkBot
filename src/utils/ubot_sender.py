import asyncio

from telethon import client, events

from src.config.bot_config import BotConfig


#
# @client.on(events.NewMessage(chats=BotConfig.work_bot_chat_id))
# async def handle_contacts(event: events.NewMessage.Event) -> None:
#     await event.reply("Получил контакты")


async def get_contact_by_phone(phone_number: int) -> dict:
    async with BotConfig.tele_ubot:
        tg_contact = BotConfig.tele_ubot.get_entity(phone_number)
    return tg_contact


async def get_contacts_from_list_by_ubot(contacts_list: list) -> list:
    contacts_list = list(map(int, contacts_list))
    contacts = [await get_contact_by_phone(contact) for contact in contacts_list]
    return contacts
