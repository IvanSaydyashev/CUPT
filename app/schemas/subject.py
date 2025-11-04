from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class SubjectBase(BaseModel):
    name: str


class SubjectCreate(SubjectBase):
    creator_id: UUID
    group_id: UUID | None = None
    class Config:
        from_attributes = True


class SubjectRead(SubjectBase):
    subject_id: UUID
    creator_id: UUID
    group_id: UUID | None
    created_at: datetime

    class Config:
        from_attributes = True
