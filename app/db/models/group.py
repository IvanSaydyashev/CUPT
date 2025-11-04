import enum

from sqlalchemy import (
    Column,
    Text,
    Enum,
    DateTime,
    func,
    UUID,
    String,
    Integer,
    Boolean,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from app.db.base import Base

import uuid


class GroupType(enum.Enum):
    STUDY = "study"
    HOBBY = "hobby"
    OTHER = "other"


class Group(Base):
    __tablename__ = "groups"

    group_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    group_type = Column(Enum(GroupType), nullable=False, default=GroupType.STUDY)
    max_members = Column(Integer, nullable=True)
    is_private = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    creator_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="Set NULL"),
        nullable=True,
    )

    creator = relationship(
        "User", back_populates="created_groups", foreign_keys=[creator_id]
    )

    members = relationship("GroupMember", back_populates="group")
    subjects = relationship("Subject", back_populates="group")
    study_sessions = relationship("StudySession", back_populates="group")
