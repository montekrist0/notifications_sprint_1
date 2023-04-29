from pydantic import BaseModel, Field


class BulkMails(BaseModel):
    group_id: str | None = Field(default=None)
    content: str
