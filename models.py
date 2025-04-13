from pydantic import BaseModel
from typing import Optional
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class JournalEntry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime = Field(default_factory=datetime.utcnow)
    entry: str
    emotion_detected: Optional[str]

class MoodEntry(BaseModel):
    date: str
    mood_rating: int
    mood_comment: str
    