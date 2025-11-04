from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class SessionIntervalBase(BaseModel):
    start_time: datetime
    end_time: datetime


class SessionIntervalCreate(SessionIntervalBase):
    session_id: UUID
    class Config:
        from_attributes = True

class SessionIntervalRead(SessionIntervalBase):
    interval_id: UUID
    session_id: UUID

    class Config:
        from_attributes = True
