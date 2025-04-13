from fastapi import APIRouter, Depends
from sqlmodel import Session
from datetime import datetime

from models import JournalEntry
from db import get_session
from utils.emotion import detect_emotion

router = APIRouter()

@router.post("/")
async def save_journal(payload: JournalEntry, session: Session = Depends(get_session)):
    # Emotion detection
    emotion = detect_emotion(payload.entry)

    entry = JournalEntry(
        date=datetime.today().date(),
        entry=payload.entry,
        emotion_detected=emotion
    )
    session.add(entry)
    session.commit()
    session.refresh(entry)
    return {"message": "Journal entry saved", "data": entry}

@router.get("/")
async def get_all_journals(session: Session = Depends(get_session)):
    journals = session.query(JournalEntry).all()
    return {"journals": journals}
