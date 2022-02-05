from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from models import db_commands
from loader import dp


@dp.message_handler(Command("create_task"))
async def create_task(message: types.Message, state: FSMContext):
    await message.answer(f"Давай заведем задачу. Отвечай на вопросы честно и мы что-нибудь придумаем.")
    await state.set_state("task_name")
    await message.answer("Введи имя задачи")


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
    await message.answer(str(task))
    await state.reset_state()


@dp.message_handler(Command("list_tasks"))
async def list_tasks(message: types.Message):
    tasks = await db_commands.list_tasks(message.from_user.id)
    if len(tasks) > 0:
        await message.answer("Вот твои незавершенные задачи")
        for task in tasks:
            await message.answer(str(task))
    else:
        await message.answer("У тебя нет задач. Но ты можешь создать одну командой /create_task")

