def find_upper(text):
    for char in text:
        if char.isupper():
            return(char)


text = input("Enter a word or a sentence: ")
print(find_upper(text))
