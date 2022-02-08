from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

task_keyboard = InlineKeyboardMarkup(
    row_width=5,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Запуск",
                callback_data="task_start"
            ),
            InlineKeyboardButton(
                text="Остановка",
                callback_data="task_stop"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Завершить",
                callback_data="task_finish"
            ),
            InlineKeyboardButton(
                text="Редактировать",
                callback_data="task_edit"
            ),
        ],
    ]
)
