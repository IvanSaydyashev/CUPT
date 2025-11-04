from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from app.db.models.group import GroupType


class GroupBase(BaseModel):
    name: str
    description: str | None = None
    group_type: GroupType = GroupType.STUDY
    max_members: int | None = None
    is_private: bool = False


class GroupCreate(GroupBase):
    hashed_password: str | None = None
    creator_id: UUID = None
    class Config:
        from_attributes = True

class GroupRead(GroupBase):
    group_id: UUID
    hashed_password: str | None
    created_at: datetime

    class Config:
        from_attributes = True
