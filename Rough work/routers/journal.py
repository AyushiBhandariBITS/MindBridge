from fastapi import APIRouter
from datetime import datetime
from models import JournalEntry# type: ignore
from utils.emotion import detect_emotion # type: ignore

journals=[]
router = APIRouter()

@router.post("/")
async def save_journal(payload: JournalEntry):
    print("finding emotion")
    emotion = detect_emotion(payload.entry)
    print("emotion found")
    print(emotion)
    print("saving journal")
    
    entry = JournalEntry(
        date=datetime.today().date().strftime("%Y-%m-%d"),
        entry=payload.entry,
        emotion_detected=emotion
    )
    print("journal saved")
    print(entry)
    journals.append(entry)
    return {"message": "Journal entry saved", "data": entry}

@router.get("/")
async def get_all_journals():
    return {"journals": journals}
