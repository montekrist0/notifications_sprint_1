import orjson
from bson import ObjectId
from pydantic import BaseModel, Field


def orjson_dumps(v):
    return orjson.dumps(v).decode()


class Base(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class PydanticObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise TypeError("ObjectId required")
        return str(v)


class UserInfo(Base):
    id: PydanticObjectId = Field(default_factory=ObjectId, alias="_id")
    user_id: str
    group_id: str
    email: str
    user_name: str
    allow_personal_notifications: bool = True
    allow_mass_notifications: bool = True
