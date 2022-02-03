from tortoise import Tortoise, Model, fields
from data.config import POSTGRES_URI


class AbstractBaseModel(Model):
    id = fields.UUIDField(pk=True)

    class Meta:
        abstract = True


class TimedBaseModel(AbstractBaseModel):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class DescriptionBaseModel(TimedBaseModel):
    name = fields.CharField(max_length=60)
    description = fields.TextField(max_length=255)

    class Meta:
        abstract = True


async def init_db():
    await Tortoise.init(
        db_url=POSTGRES_URI,
        modules={'models': ['models.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
