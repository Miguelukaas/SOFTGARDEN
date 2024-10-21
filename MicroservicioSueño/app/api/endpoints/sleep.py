from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.db.session import get_db
from app.models.sleep_session import SleepSession
from app.schemas.sleep_session import SleepSessionCreate, SleepSessionUpdate, SleepSessionOut

router = APIRouter()

@router.post("/start_sleep", response_model=SleepSessionOut)
def start_sleep(session: SleepSessionCreate, db: Session = Depends(get_db)):
    new_session = SleepSession(baby_name=session.baby_name)
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

@router.post("/end_sleep/{session_id}", response_model=SleepSessionOut)
def end_sleep(session_id: int, session_update: SleepSessionUpdate, db: Session = Depends(get_db)):
    session = db.query(SleepSession).filter(SleepSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Sesión de sueño no encontrada")
    
    session.end_time = session_update.end_time
    db.commit()
    db.refresh(session)
    return session

@router.get("/sleep_sessions/{baby_name}", response_model=list[SleepSessionOut])
def get_sessions(baby_name: str, db: Session = Depends(get_db)):
    sessions = db.query(SleepSession).filter(SleepSession.baby_name == baby_name).all()
    return sessions
