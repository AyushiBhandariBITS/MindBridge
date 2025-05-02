from pydantic import BaseModel


class JournalEntry(BaseModel):
    date: str
    entry: str
    emotion_detected: str

class MoodEntry(BaseModel):
    date: str
    mood_rating: int
    mood_comment: str
    