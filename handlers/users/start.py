from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from models import db_commands
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await message.answer("Добро пожаловать к нам. Ты зарегистрирован в базе")
    await db_commands.add_user(message.from_user.id, message.from_user.username)
