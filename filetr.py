import json
import os
import re
from my_packages import module1, module2, module3

def main():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print("Config file error.")
        return

    fname = config["file_name"]
    if not os.path.exists(fname):
        print("File not found.")
        return

    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    chars_count = len(content)
    words_count = len(content.split())
    sentences_count = len(re.split(r'[.!?]+', content)) - 1

    print(f"File: {fname}")
    print(f"Stats -> Chars: {chars_count}, Words: {words_count}, Sentences: {sentences_count}")
    
    lang_detected = module3.LangDetect(content, "lang")
    print(f"Detected Language: {lang_detected}")

    limit_chars = config["max_chars"]
    limit_words = config["max_words"]
    limit_sent = config["max_sentences"]

    final_text = ""
    current_sentences = re.split(r'([.!?]+)', content)
    
    temp_text = ""
    sent_counter = 0

    for i in range(0, len(current_sentences)-1, 2):
        sentence_part = current_sentences[i] + current_sentences[i+1]
        
        if len(temp_text) + len(sentence_part) > limit_chars: break
        if len((temp_text + sentence_part).split()) > limit_words: break
        if sent_counter >= limit_sent: break
        
        temp_text += sentence_part
        sent_counter += 1
        
    final_text = temp_text

    print(f"\nText prepared for translation ({len(final_text)} chars).")

    mod_name = config["module_name"]
    target = config["target_language"]
    
    translator = None
    if mod_name == "module1": translator = module1
    elif mod_name == "module2": translator = module2
    elif mod_name == "module3": translator = module3
    else: translator = module1

    translated = translator.TransLate(final_text, 'auto', target)

    output = config["output"]
    if output == "screen":
        print(f"\n--- Translated to {target} via {mod_name} ---")
        print(translated)
        print("Ok")
    elif output == "file":
        out_name = f"{os.path.splitext(fname)[0]}_{target}.txt"
        with open(out_name, "w", encoding="utf-8") as f:
            f.write(translated)
        print("Ok")

if __name__ == "__main__":
    main()