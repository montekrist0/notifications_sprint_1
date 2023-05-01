from pydantic import BaseModel


class Mail(BaseModel):
    user_name: str
    email: str
    content: str
