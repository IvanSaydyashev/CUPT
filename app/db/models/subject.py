from sqlalchemy import Column, ForeignKey, String, DateTime, func, UUID
from sqlalchemy.orm import relationship

from app.db.base import Base

import uuid


class Subject(Base):
    __tablename__ = "subjects"

    subject_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    creator_id = Column(
        UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE"), index=True
    )
    group_id = Column(
        UUID(as_uuid=True),
        ForeignKey("groups.group_id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    creator = relationship("User", back_populates="subjects")
    group = relationship("Group", back_populates="subjects")
    study_sessions = relationship("StudySession", back_populates="subject")
