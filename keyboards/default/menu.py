from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Новая задача"),
            KeyboardButton(text="Новый проект")
        ],
        [
            KeyboardButton(text="Задачи"),
            KeyboardButton(text="Проекты"),
            KeyboardButton(text="Настройки")
        ]
    ],
    resize_keyboard=True
)
