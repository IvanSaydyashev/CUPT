from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from app.db.models.group_member import GroupRole


class GroupMemberBase(BaseModel):
    role: GroupRole = GroupRole.MEMBER


class GroupMemberCreate(GroupMemberBase):
    group_id: UUID
    user_id: UUID
    class Config:
        from_attributes = True

class GroupMemberRead(GroupMemberBase):
    group_id: UUID
    user_id: UUID
    joined_at: datetime

    class Config:
        from_attributes = True
