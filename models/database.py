from tortoise import Tortoise, Model, fields
from data.config import POSTGRESURI


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
    name = fields.StringField(max_length=60)
    description = fields.StringField(max_length=255)

    class Meta:
        abstract = True


async def init_db():
    await Tortoise.init(
        db_url=POSTGRESURI,
        modules={'models': ['utils.db_api.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()
