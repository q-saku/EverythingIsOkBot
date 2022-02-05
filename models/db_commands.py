import asyncpg

from models.models import Task, User, Project, Meeting


async def add_user(user_id, name):
    return await User.get_or_create(id=user_id, name=name)


async def get_user(user_id):
    return await User.filter(id=user_id).get_or_none()


async def add_task(**kwargs):
    kwargs["user"] = await get_user(kwargs.get("user"))
    return await Task.create(**kwargs)


async def get_task(task_id):
    return await Task.filter(id=task_id).first()


async def list_tasks(user_id):
    return await Task.filter(user_id=user_id).all()

