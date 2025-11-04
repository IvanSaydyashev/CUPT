import enum

from sqlalchemy import Column, ForeignKey, Enum, DateTime, func, UUID
from sqlalchemy.orm import relationship

from app.db.base import Base

import uuid


class SessionStatus(enum.Enum):
    ACTIVE = "active"
    PAUSED = "paused"
    FINISHED = "finished"


class StudySession(Base):
    __tablename__ = "study_sessions"

    session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(
        UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE"), index=True
    )
    group_id = Column(
        UUID(as_uuid=True),
        ForeignKey("groups.group_id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    subject_id = Column(
        UUID(as_uuid=True),
        ForeignKey("subjects.subject_id", ondelete="CASCADE"),
        index=True,
    )
    status = Column(Enum(SessionStatus), nullable=False, default=SessionStatus.ACTIVE)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="study_sessions")
    group = relationship("Group", back_populates="study_sessions")
    subject = relationship("Subject", back_populates="study_sessions")
    intervals = relationship(
        "SessionInterval", back_populates="session", cascade="all, delete"
    )
