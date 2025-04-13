from fastapi import APIRouter
from pydantic import BaseModel
from utils.translation import translate_text, detect_language
from utils.emotion import detect_emotion
from utils.prompts import build_prompt
import openai
from openai import OpenAI
import os
# Swap out OpenAI for OpenRouter
#openai.api_key = os.getenv("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")
#openai.api_base = "https://openrouter.ai/api/v1/chat/completions"
#client = OpenAI(api_key="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")
client = OpenAI(
    api_key="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",  # your OpenRouter API key
    base_url="https://openrouter.ai/api/v1",  # OpenRouter's base URL
    default_headers={
        "HTTP-Referer": "http://localhost",  # or your project domain
        "X-Title": "MindBridge",  # your app name or purpose
    }
)

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_lang: str = None

@router.post("/")
async def chat_with_ai(payload: ChatRequest):
    try:
        user_input = payload.message
        lang = payload.user_lang or detect_language(user_input)       
        translated_input = translate_text(user_input, lang, "en")
        emotion = detect_emotion(translated_input)
        prompt = build_prompt(translated_input, emotion)
        # Call OpenAI API (or DeepSeek API) here
        response = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",
            messages=[{"role": "system", "content": prompt},
                      {"role": "user", "content": translated_input}],
            temperature=0.8,
        )
        reply = response.choices[0].message.content.strip()
        translated_reply = translate_text(reply, "en", lang)
        return {
            "reply": translated_reply,
            "emotion": emotion,
            "language": lang
        }
    except Exception as e:
        print(f"Error during chat process: {e}")
        return {"error": "An error occurred while processing your request."}
