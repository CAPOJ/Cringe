from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard_menu=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить свой код"),
            KeyboardButton(text="Получить свой код"),
        ],
        [
            KeyboardButton(text="Показать результат"),
        ]
    ],
    resize_keyboard=True
)