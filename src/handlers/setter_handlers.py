from aiogram import Dispatcher

from .handlers import router


def set_routers(dp: Dispatcher):
    dp.include_router(router)
