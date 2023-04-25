from pydantic import BaseModel


class PersonalSelection(BaseModel):
    user_id: str
    films: list[str]
