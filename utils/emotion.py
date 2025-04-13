from transformers import pipeline

emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

def detect_emotion(text):
    results = emotion_model(text)
    if isinstance(results, list) and len(results) > 0 and isinstance(results[0], dict):
        return results[0].get("label", "neutral")
    return "neutral"

