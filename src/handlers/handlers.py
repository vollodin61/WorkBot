import asyncio

from aiogram import Router, Bot, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.markdown import hlink

from src.config.conf import Emo, BotConfig
from src.config.conf import debug_logger, error_logger, RedisConfig, info_logger

router = Router()


@router.message(CommandStart(deep_link=True))
async def cmd_start_with_deeplink_handler(msg: Message, command: CommandObject, bot: Bot):
    debug_logger("ДИПЛИНК ПОЙМАН!")


@router.message(CommandStart())
async def cmd_start_handler(msg: Message):
    debug_logger("Сработал обычный команда старт!")
    if msg.chat.id == BotConfig.PS_CHAT_ID:
        await msg.answer("Здравствуйте, Павел Сергеевич! 🤗")
    else:
        await msg.answer("Hello, my friend! 🤗")


@router.message(Command('cancel'))
async def cmd_cancel_handler(msg: Message, state: FSMContext):
    await state.clear()
    await msg.answer("Обнулил state, отмена предыдущего действия")


@router.message(lambda msg: msg.left_chat_member is not None)
async def left_members_handler(msg: Message):
    """Удаляем сообщение об уходе участника."""
    await msg.delete()


@router.message(Command('help'))
async def cmd_help_handler(msg: Message):
    await msg.answer("Тут ещё нет текста для команды /help")


@router.message(Command("homework"))
async def give_homework_handler(msg: Message, bot: Bot):
    await bot.send_message(chat_id=msg.from_user.id, text="await get_homework_text()")
    await asyncio.sleep(2)
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)


@router.message(F.text == 'Ао')
async def print_state_handler(msg: Message, state: FSMContext):
    data = await state.get_data()
    current_state = await state.get_state()
    await msg.answer(text=f"{data =}")
    await msg.answer(text=f"{current_state =}")


@router.message(F.text == 'Д')
async def delete_user_handler(msg: Message, state: FSMContext):
    await msg.answer("Удалил тебя из базы")
    info_logger(f"Удалили пользователя {msg.from_user.id} из базы")
