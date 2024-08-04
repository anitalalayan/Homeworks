def word_count(text):
    return len(text.split())

def character_count(text):
    return len(text)

def find_word(text, word):
    return text.find(word)

def replace_word(text, old_word, new_word):
    return text.replace(old_word, new_word)


text_operations = {
    'word_count': word_count,
    'character_count': character_count,
    'find_word': find_word,
    'replace_word': replace_word
}

def process_text(text, operation, **kwargs):
    return text_operations.get(operation)(text,**kwargs)


text = input("Enter a text: ").lower()

print(process_text(text, 'word_count'))
print(process_text(text, 'character_count'))
print(process_text(text, 'find_word', word='hello'))
print(process_text(text, 'replace_word', old_word='hello', new_word='hi'))
