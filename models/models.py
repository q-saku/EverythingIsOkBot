from tortoise import fields
from models.database import AbstractBaseModel, TimedBaseModel, DescriptionBaseModel


class User(TimedBaseModel):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=100)


class Task(DescriptionBaseModel):
    status = fields.TextField()
    time_spent = fields.DatetimeField()
    date_finished = fields.DatetimeField()
    user = fields.ForeignKeyField('models.User', related_name='tasks')

    def __repr__(self):
        return f"""
        Задача: {self.name}
        Описание: {self.description}
        """


class Project(DescriptionBaseModel):
    tasks = fields.ForeignKeyField('models.Task', related_name='project')
    users = fields.ManyToManyField('models.User', related_name='projects')


class Meeting(DescriptionBaseModel):
    __tablename__ = "meeting"
    date_start = fields.DatetimeField()
    date_stop = fields.DatetimeField()
    task = fields.ForeignKeyField('models.Task', related_name='meetings')
    user = fields.ForeignKeyField('models.User', related_name='meetings')


class Settings(AbstractBaseModel):
    user = fields.OneToOneField('models.User', related_name='settings')

