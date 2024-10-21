from sqlalchemy import Column, Integer, String, DateTime
from app.db.base import Base
from datetime import datetime

class SleepSession(Base):
    __tablename__ = 'sleep_sessions'
    
    id = Column(Integer, primary_key=True, index=True)
    baby_name = Column(String(100), nullable=False)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    
    def __repr__(self):
        return f"<SleepSession {self.baby_name}, Start: {self.start_time}, End: {self.end_time}>"
