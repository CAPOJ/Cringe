from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import keyboard_menu
from loader import dp


@dp.message_handler(Command("menu"))
async def menu(message: types.Message):
    await message.answer("Выберите одно из действий в меню",reply_markup=keyboard_menu)