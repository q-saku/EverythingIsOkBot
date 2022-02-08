from aiogram import types
from aiogram.dispatcher.filters import Command
from keyboards.default.menu import main_menu

from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Вот твое меню", reply_markup=main_menu)


# async def list_daily_tasks():
#     markup = await dialy_tasks_keyboard()