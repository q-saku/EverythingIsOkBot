from aiogram import executor

from loader import dp
from models.database import init_db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    import middlewares
    import filters
    import handlers
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    await init_db()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

