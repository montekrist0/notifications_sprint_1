from pydantic import BaseModel


class Welcome(BaseModel):
    user_id: str
