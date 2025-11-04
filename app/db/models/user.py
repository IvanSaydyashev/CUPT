from sqlalchemy import Column, Integer, String, DateTime, func, UUID
from sqlalchemy.orm import relationship

from app.db.session import Base

import uuid


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=True)
    first_name = (Column(String, nullable=True),)
    last_name = (Column(String, nullable=True),)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    groups = relationship("GroupMember", back_populates="user")
    created_groups = relationship("Group", back_populates="creator")
    subjects = relationship("Subject", back_populates="creator")
    study_sessions = relationship("StudySession", back_populates="user")
