from my_packages import module1

print("--- Модуль 1 (Googletrans) ---")
print(f"Перевод 'Hello' на українську: {module1.TransLate('Hello', 'en', 'uk')}")
print(f"Мова речення 'Добрий день': {module1.LangDetect('Добрий день', 'all')}")
print(f"Код мови 'ukrainian': {module1.CodeLang('ukrainian')}")
print(f"Список перекладу 'Hello' на інших мовах: {module1.LanguageList('screen', 'Hello')}")