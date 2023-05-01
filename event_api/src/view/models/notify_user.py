from pydantic import BaseModel


class NotifyUser(BaseModel):
    user_id: str
    content: str
