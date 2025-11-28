from googletrans import Translator, LANGUAGES

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = Translator()
        src_lang = 'auto' if scr == 'auto' else scr
        result = translator.translate(text, src=src_lang, dest=dest)
        return result.text
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        translator = Translator()
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"Language: {detection.lang}, Confidence: {detection.confidence}"
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return "Error: Language not found"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        translator = Translator()
        lines = [f"{'N':<4} {'Language':<20} {'ISO':<10} {'Text'}"]
        lines.append("-" * 50)
        
        for i, (code, name) in enumerate(list(LANGUAGES.items())[:25], 1):
            row = f"{i:<4} {name.capitalize():<20} {code:<10}"
            if text:
                try:
                    trans = translator.translate(text, dest=code).text
                    row += f" {trans}"
                except:
                    row += " Error"
            lines.append(row)
            
        result = "\n".join(lines)
        
        if out == "screen":
            print(result)
        elif out == "file":
            with open("languages_list_gtrans.txt", "w", encoding="utf-8") as f:
                f.write(result)
        return "Ok"
    except Exception as e:
        return f"Error: {e}"