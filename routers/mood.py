from fastapi import APIRouter
from models import MoodEntry
from datetime import datetime

mood_entries = []

router = APIRouter()

@router.post("/")
async def track_mood(payload: MoodEntry):
    # Store mood entry
    entry = {
        "date": datetime.today().date().strftime("%Y-%m-%d"),
        "mood_rating": payload.mood_rating,
        "mood_comment": payload.mood_comment,
    }
    mood_entries.append(entry)
    return {"message": "Mood entry saved", "data": entry}

@router.get("/")
async def get_all_mood_entries():
    return {"mood_entries": mood_entries}
