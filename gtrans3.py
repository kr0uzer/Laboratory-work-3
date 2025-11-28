from my_packages import module2

print("--- Модуль 2 (Deep Translator) в докері ---")
print(f"Перевести 'Docker is cool' на українську: {module2.TransLate('Docker is cool', 'auto', 'uk')}")
print(f"Код мови 'german': {module2.CodeLang('german')}")
print(f"Список перекладів 'Hello, World!' на інші мови: {module2.LanguageList("screen", "Hello, world!")}")