from telethon import TelegramClient

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from emoji import emojize

from .base_config import env
from .redis_config import RedisConfig


class BotConfig:
    bot_token = env("TOKEN")

    web_server_host = env("WEB_SERVER_HOST")
    web_server_port = int(env("WEB_SERVER_PORT"))

    base_webhook_url = env("BASE_WEBHOOK_URL")
    webhook_path = env("WEBHOOK_PATH")

    webhook_url = f"{base_webhook_url}{webhook_path}"
    webhook_secret_token = env("WEBHOOK_SECRET")

    admins_ids = [int(_) for _ in env("ADMINS_IDS").split(", ")]

    redis_host = env("REDIS_HOST")
    redis_port = int(env("REDIS_PORT"))
    redis = RedisConfig.get_connection()
    red_storage = RedisStorage(redis)

    dp = Dispatcher(storage=red_storage)
    bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode="HTML"))
    scheduler = AsyncIOScheduler(
        timezone="UTC",
        jobstores={"default": RedisJobStore(host=redis_host, port=redis_port, db=0)},
    )

    tele_ubot_id: int = int(env("TELE_UBOT_ID"))
    tele_ubot_hash: str = env("TELE_UBOT_HASH")

    tele_ubot = TelegramClient(
        session="MinZKH_bot",
        api_id=tele_ubot_id,
        api_hash=tele_ubot_hash,
        device_model="POCO POCO X3 Pro",
        app_version="Telegram Android 11.9.0",
        system_version="Android 12",
        lang_code="ru",
    )

    MY_CHAT_ID: int = int(env("MY_CHAT_ID"))
    PS_CHAT_ID: int = int(env("PS_CHAT_ID"))
    INVITE_CHAT_ID: int = int(env("INVITE_CHAT_ID"))
    WORK_BOT_CHAT_ID: int = int(env("WORK_BOT_CHAT_ID"))

#
# class MyStates(StatesGroup):  # todo
#    ... #


class Emo:
    #  Эмодзи тут -> нажми Meta + .
    @staticmethod
    def get_emoji(smile):
        return emojize(smile, variant="emoji_type")

    ruble = get_emoji("₽")
    big_smile = get_emoji(":grinning_face_with_big_eyes:")
    hugs = get_emoji(":smiling_face_with_open_hands:")
    hand_over_mouth = get_emoji(":face_with_hand_over_mouth:")
    hundred = get_emoji(":hundred_points:")
    quiet = get_emoji(":shushing_face:")
    heart = get_emoji("❤️")
    omg_cat_face = get_emoji("🙀")
    red_exclamation = get_emoji("❗️")
    nerd_face = get_emoji(":nerd_face:")
    sunglasses = get_emoji("😎")
    explosive_head = get_emoji("🤯")
    hi = get_emoji("👋")
    just_smile = get_emoji("🙂")
    zero = get_emoji("0️⃣")
    one = get_emoji("1️⃣")
    two = get_emoji("2️⃣")
    three = get_emoji("3️⃣")
    four = get_emoji("4️⃣")
    five = get_emoji("5️⃣")
    six = get_emoji("6️⃣")
    seven = get_emoji("7️⃣")
    eight = get_emoji("8️⃣")
    nine = get_emoji("9️⃣")
    ten = get_emoji("🔟")
    hz = get_emoji("🤷‍♂️")
    please_eyes = get_emoji("🥺")
    please = get_emoji("🙏")
    arrow_left = get_emoji("⬅️")
    arrow_right = get_emoji("➡️️")
    arrow_up = get_emoji("⬆️")
    arrow_down = get_emoji("⬇️")
    write = get_emoji("✍️")
    confused = get_emoji("😕")
    airplane = get_emoji("🛫")

    nums_for_quests = [one, two, three, four]
