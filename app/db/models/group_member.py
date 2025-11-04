import enum

from sqlalchemy import Column, ForeignKey, Enum, DateTime, func, UUID
from sqlalchemy.orm import relationship

from app.db.session import Base


class GroupRole(enum.Enum):
    MEMBER = "member"
    ADMIN = "admin"


class GroupMember(Base):
    __tablename__ = "group_members"

    group_id = Column(
        UUID(as_uuid=True),
        ForeignKey("groups.group_id", ondelete="CASCADE"),
        primary_key=True,
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True,
    )
    role = Column(Enum(GroupRole), nullable=False, default=GroupRole.MEMBER)
    joined_at = Column(DateTime(timezone=True), server_default=func.now())

    group = relationship("Group", back_populates="members")
    user = relationship("User", back_populates="groups")
