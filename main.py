from fastapi import FastAPI
from routers import chat, resources, journal, mood, wellness
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/chat")
app.include_router(resources.router, prefix="/resources")
app.include_router(journal.router, prefix="/journal", tags=["Journal"])
app.include_router(mood.router, prefix="/mood", tags=["Mood Tracking"])
app.include_router(wellness.router, prefix="/wellness")

@app.get("/")
def root():
    return {"message": "Ola, MindBridge API is running!"}
