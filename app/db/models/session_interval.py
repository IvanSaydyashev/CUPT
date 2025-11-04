from sqlalchemy import Column, ForeignKey, DateTime, UUID
from sqlalchemy.orm import relationship

from app.db.base import Base

import uuid


class SessionInterval(Base):
    __tablename__ = "session_intervals"

    interval_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(
        UUID(as_uuid=True),
        ForeignKey("study_sessions.session_id", ondelete="CASCADE"),
        index=True,
    )
    start_time = Column(DateTime(timezone=True), nullable=False)
    end_time = Column(DateTime(timezone=True), nullable=True)

    session = relationship("StudySession", back_populates="intervals")
