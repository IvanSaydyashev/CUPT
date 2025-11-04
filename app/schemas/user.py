import uuid
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None


class UserCreate(UserBase):
    telegram_id: int


class UserRead(UserBase):
    user_id: uuid.UUID
    telegram_id: int
    created_at: datetime

    class Config:
        orm_mode = True
