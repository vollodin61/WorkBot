#  todo выбрать нужные отложенные
#   придумать логику отложенных сообщений.




# from datetime import datetime, timedelta
# from typing import Iterable
#
# from apscheduler.triggers.interval import IntervalTrigger
#
# from src.bot.config.bot_config import BotConfig
# from src.bot.db.database import add_user_to_removed
# from src.bot.utils.bot_utils import send_personal_notification
# from src.bot.utils.safe_call_decorator import safe_call_dec
# from src.config import error_logger, RedisConfig
#
#
# @safe_call_dec
# async def send_interval_reminder(chat_id, text, interval):
#     BotConfig.scheduler.add_job(
#         send_personal_notification,
#         trigger=IntervalTrigger(minutes=int(interval)),
#         id=f'reminder:{chat_id}',
#         replace_existing=True,
#         kwargs={"chat_id": chat_id, "text": text}
#     )
#
#
# @safe_call_dec
# async def add_many_reminders(entities: Iterable, text, interval):
#     for entity in entities:
#         await send_interval_reminder(chat_id=entity,
#                                      text=text,
#                                      interval=interval)
#
#
# @safe_call_dec
# async def msg_deleter(msg_id, chat_id):
#     await BotConfig.bot.delete_message(chat_id=chat_id, message_id=msg_id)
#
#
# @safe_call_dec
# async def ban_user_from_chat(chat_id, user_id):
#     await BotConfig.bot.ban_chat_member(chat_id=chat_id, user_id=user_id)
#
#
# @safe_call_dec
# async def unban_user_from_chat(chat_id, user_id):
#     await BotConfig.bot.unban_chat_member(chat_id=chat_id, user_id=user_id)
#
#
# @safe_call_dec
# async def add_user_to_removed_table(chat_id, user_id):
#     await add_user_to_removed(chat_id=chat_id, tg_id=user_id)
#
#
# @safe_call_dec
# async def auto_ban_unban_n_del_verif_msg(msg_id, chat_id, user_id):
#     msg_del_job = BotConfig.scheduler.add_job(
#         msg_deleter,
#         id=f'{chat_id}:{user_id}:{msg_id}',
#         trigger="date",
#         run_date=datetime.now() + timedelta(seconds=600),
#         kwargs={"msg_id": msg_id, "chat_id": chat_id},
#         replace_existing=True
#     )
#
#     ban_user_job = BotConfig.scheduler.add_job(
#         ban_user_from_chat,
#         id=f'{chat_id}:ban:{user_id}',
#         trigger="date",
#         run_date=datetime.now() + timedelta(seconds=601),
#         kwargs={"chat_id": chat_id, "user_id": user_id},
#         replace_existing=True
#     )
#
#     unban_user_job = BotConfig.scheduler.add_job(
#         unban_user_from_chat,
#         id=f'{chat_id}:unban:{user_id}',
#         trigger="date",
#         run_date=datetime.now() + timedelta(seconds=602),
#         kwargs={"chat_id": chat_id, "user_id": user_id},
#         replace_existing=True
#     )
#
#     add_to_removed_job = BotConfig.scheduler.add_job(
#         add_user_to_removed_table,
#         id=f'{chat_id}:removed:{user_id}',
#         trigger="date",
#         run_date=datetime.now() + timedelta(seconds=603),
#         kwargs={"chat_id": chat_id, "user_id": user_id},
#         replace_existing=True
#     )
#     name = f"verification:{chat_id}:{user_id}"
#
#     await RedisConfig.get_connection().hset(name=name,
#                                             mapping={
#                                                 "msg_del_job_id": msg_del_job.id,
#                                                 "ban_user_job_id": ban_user_job.id,
#                                                 "unban_user_job_id": unban_user_job.id,
#                                                 "add_to_removed_job_id": add_to_removed_job.id
#                                             })
#
#
# async def remove_scheduled_jobs_n_del_verif_msg(chat_id, user_id):
#     name = f"verification:{chat_id}:{user_id}"
#     msg_id = await RedisConfig.get_connection().hget(name=name, key="msg_id")
#     msg_del_job_id = await RedisConfig.get_connection().hget(name=name, key="msg_del_job_id")
#     ban_job_id = await RedisConfig.get_connection().hget(name=name, key="ban_user_job_id")
#     unban_job_id = await RedisConfig.get_connection().hget(name=name, key="unban_user_job_id")
#     add_to_removed_job_id = await RedisConfig.get_connection().hget(name=name, key="add_to_removed_job_id")
#
#     try:
#         await BotConfig.bot.delete_message(chat_id=int(chat_id), message_id=int(msg_id))
#     except Exception as e:
#         error_logger(repr(e))
#
#     await cancel_ban_scheduled_job(ban_job_id)
#     await cancel_msg_del_job(msg_del_job_id)
#     await cancel_unban_scheduled_job(unban_job_id)
#     await cancel_add_to_removed_job(add_to_removed_job_id)
#
#
# async def cancel_ban_scheduled_job(ban_job_id):
#     try:
#         BotConfig.scheduler.remove_job(ban_job_id)
#     except Exception as e:
#         error_logger(f"Возможно ban-job уже была удалена или что ещё случилось, ОШИБКА: {repr(e)}")
#
#
# async def cancel_msg_del_job(msg_del_job_id):
#     try:
#         BotConfig.scheduler.remove_job(msg_del_job_id)
#     except Exception as e:
#         error_logger(f"Возможно msg_del-job уже была удалена или что ещё случилось, ОШИБКА: {repr(e)}")
#
#
# async def cancel_unban_scheduled_job(unban_job_id):
#     try:
#         BotConfig.scheduler.remove_job(unban_job_id)
#     except Exception as e:
#         error_logger(f"Возможно unban-job уже была удалена или что ещё случилось, ОШИБКА: {repr(e)}")
#
#
# async def cancel_add_to_removed_job(add_to_removed_job_id):
#     try:
#         BotConfig.scheduler.remove_job(add_to_removed_job_id)
#     except Exception as e:
#         error_logger(f"Возможно add_to_removed_job уже была удалена или что ещё случилось, ОШИБКА: {repr(e)}")
