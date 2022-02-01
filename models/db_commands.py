from models.models import Task


async def add_task(**kwargs):
    new_task = await Task(**kwargs).create()
    return new_task


async def get_task(task_id):
    task = Task.query.where(Task.id == task_id).gino.first()


async def list_tasks():
    return await Task.query.gino.all()

