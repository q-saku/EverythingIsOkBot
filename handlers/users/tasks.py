from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.types import ReplyKeyboardRemove, callback_query, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils import callback_data

from keyboards.default.menu import main_menu
from keyboards.inline.task import task_keyboard
from models import db_commands
from loader import dp


@dp.message_handler(Command("create_task"))
async def create_task(message: types.Message, state: FSMContext):
    await message.answer(f"Давай заведем задачу. Отвечай на вопросы честно и мы что-нибудь придумаем.")
    await state.set_state("task_name")
    await message.answer("Введи имя задачи", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(state="task_name")
async def enter_task_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state("task_description")
    await message.answer("Введи описание задачи")


@dp.message_handler(state="task_description")
async def enter_task_description(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    task_data = await state.get_data()
    task = await db_commands.add_task(name=task_data["name"],
                                      description=task_data["description"],
                                      user=message.from_user.id)
    await message.answer("Задача успешно заведена")
    await message.answer(str(task), reply_markup=main_menu)
    await state.reset_state()


@dp.message_handler(Command("list_tasks"))
async def list_tasks(message: types.Message):
    tasks = await db_commands.list_tasks(message.from_user.id)
    if len(tasks) > 0:
        keyboard = InlineKeyboardMarkup(row_width=1)
        for task in tasks:
            button = InlineKeyboardButton(text=task.name, callback_data='task_id:' + str(task.id))
            keyboard.insert(button)
        await message.answer("Вот твои незавершенные задачи", reply_markup=keyboard)
    else:
        await message.answer("У тебя нет задач. Но ты можешь создать одну командой /create_task")


@dp.callback_query_handler(Text(startswith="task_id"))
async def get_task(call: types.CallbackQuery):
    task = await db_commands.get_task(call.data.split(':')[1])
    await call.message.answer(str(task), reply_markup=task_keyboard)

# @dp.callback_query_handler(Text(startswith="task_start")
# async def start_task(call: types.CallbackQuery):
#     pass
#
#
# @dp.callback_query_handler(callback_data="task_stop")
# async def stop_task(call: types.CallbackQuery):
#     pass
#
#
# @dp.callback_query_handler(callback_data="task_edit")
# async def edit_task(call: types.CallbackQuery):
#     pass
#
#
# @dp.callback_query_handler(callback_data="task_finish")
# async def finish_task(call: types.CallbackQuery):
#     pass
