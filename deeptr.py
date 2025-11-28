from my_packages import module3

print("--- Модуль 3 (Deep + LangDetect) ---")
print(f"Перевод 'Hello': {module3.TransLate('Hello', 'auto', 'uk')}")
print(f"Виявити мову речення 'Добрий день': {module3.LangDetect('Добрий день', 'all')}")
print(f"Код мови 'uk': {module3.CodeLang('uk')}")