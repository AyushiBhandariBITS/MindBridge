from langdetect import detect, LangDetectException
from transformers import MarianMTModel, MarianTokenizer
from functools import lru_cache

# Language mapping for Helsinki-NLP models
LANG_CODE_MAP = {
    'en': 'en',
    'fr': 'fr',
    'de': 'de',
    'es': 'es',
    'ru': 'ru',
    'it': 'it',
    'zh': 'zh',  # simplified Chinese
    'hi': 'hi',
    'ja': 'ja',
    'ko': 'ko',
}

@lru_cache(maxsize=128)
def get_translation_model(source_lang, target_lang):
    src = LANG_CODE_MAP.get(source_lang, 'en')
    tgt = LANG_CODE_MAP.get(target_lang, 'en')
    model_name = f"Helsinki-NLP/opus-mt-{src}-{tgt}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

def detect_language(text):
    try:
        # Try detecting the language
        return detect(text)
    except LangDetectException as e:
        # Catch language detection errors (e.g., empty input or failure to detect)
        print(f"Error detecting language: {e}")
        return "unknown"

def translate_text(text, source_lang, target_lang):
    if source_lang == target_lang:
        return text

    try:
        tokenizer, model = get_translation_model(source_lang, target_lang)
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated = model.generate(**inputs)
        translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
        return translated_text

    except Exception as e:
        return f"[Translation error: {str(e)}]"
