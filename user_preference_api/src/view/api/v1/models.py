from pydantic import BaseModel


class UserPreferenceInput(BaseModel):
    allow_personal_notifications: bool
    allow_mass_notifications: bool


class UserInfo(BaseModel):
    user_id: str
    group_id: str
    email: str
    user_name: str
    allow_personal_notifications: bool = True
    allow_mass_notifications: bool = True
