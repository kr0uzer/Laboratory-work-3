from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

from .module2 import TransLate, CodeLang, LanguageList

def LangDetect(text: str, set: str = "all") -> str:
    try:
        if set == "lang":
            return detect(text)
        elif set == "confidence":
            return str(detect_langs(text)[0].prob)
        else:
            res = detect_langs(text)[0]
            return f"Lang: {res.lang}, Confidence: {res.prob}"
    except Exception as e:
        return f"Error: {e}"