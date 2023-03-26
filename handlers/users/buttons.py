from aiogram import types
from loader import dp

@dp.message_handler(text="Отправить свой код")
async def buttons_test(message:types.Message):
    await message.answer(f'Ты отправил, {message.text}.')

@dp.message_handler(text="Получить свой код")
async def buttons_test(message:types.Message):
    await message.answer(f'Вот ваш код, {message.text}.')

@dp.message_handler(text="Показать результат")
async def buttons_test(message:types.Message):
    await message.answer(f'Ваш результат, 0.')