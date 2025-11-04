from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from app.db.models.study_session import SessionStatus


class StudySessionBase(BaseModel):
    status: SessionStatus = SessionStatus.ACTIVE


class StudySessionCreate(StudySessionBase):
    user_id: UUID
    subject_id: UUID
    group_id: UUID | None = None


class StudySessionRead(StudySessionBase):
    session_id: UUID
    user_id: UUID
    subject_id: UUID
    group_id: UUID | None
    created_at: datetime

    class Config:
        orm_mode = True
