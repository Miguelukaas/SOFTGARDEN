from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SleepSessionCreate(BaseModel):
    baby_name: str

class SleepSessionUpdate(BaseModel):
    end_time: datetime

class SleepSessionOut(BaseModel):
    id: int
    baby_name: str
    start_time: datetime
    end_time: Optional[datetime]

    class Config:
        orm_mode = True
