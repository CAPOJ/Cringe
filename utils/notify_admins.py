import logging
from aiogram import Dispatcher
from data.config import admin
from loader import dp

async def on_startup_notify(dp:Dispatcher):
    for admins in admin:
        try:
            text="Bot started"
            await dp.bot.send_message(chat_id=admins, text=text)
        except Exception as err:
            logging.exception(err)