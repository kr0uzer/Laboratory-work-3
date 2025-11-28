import sys
from deep_translator import GoogleTranslator

if sys.version_info >= (3, 13):
    print("Warning: Python version >= 3.13 detected.")

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translated = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> str:
    try:
        langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
        if lang in langs_dict.values():
             for name, code in langs_dict.items():
                if code == lang: return name.capitalize()
        elif lang.lower() in langs_dict:
            return langs_dict[lang.lower()]
        return "Error: Language not found"
    except Exception as e:
        return f"Error: {e}"

def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
        lines = [f"{'N':<4} {'Language':<20} {'ISO':<10} {'Text'}"]
        lines.append("-" * 50)
        
        i = 1
        for name, code in list(langs_dict.items())[:25]:
            row = f"{i:<4} {name.capitalize():<20} {code:<10}"
            if text:
                try:
                    trans = GoogleTranslator(source='auto', target=code).translate(text)
                    row += f" {trans}"
                except:
                    row += " Error"
            lines.append(row)
            i += 1
            
        result = "\n".join(lines)
        if out == "screen":
            print(result)
        elif out == "file":
            with open("languages_list_deep.txt", "w", encoding="utf-8") as f:
                f.write(result)
        return "Ok"
    except Exception as e:
        return f"Error: {e}"