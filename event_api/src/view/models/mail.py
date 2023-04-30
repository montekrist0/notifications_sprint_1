from pydantic import BaseModel


class Mail(BaseModel):
    user_name: str
    email: str
    content: str


class NotifyUser(BaseModel):
    user_id: str
    content: str
