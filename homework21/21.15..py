def uppercase(string):
    return string.upper()

def lowercase(string):
    return string.lower()

def titlecase(string):
    return string.title()

def reverse(string):
    return ''.join(reversed(string))


operations = {'Uppercase': uppercase,
              'Lowercase': lowercase,
              'TitleCase': titlecase,
              'Reversed': reverse}

def manipulate_string(s, operation):
    return operations.get(operation)(s)

operation = input("Enter an operation name (Uppercase, Lowercase, TitleCase, Reversed): ")
word = input("Enter a word you want to alter: ")

print(manipulate_string(word, operation))

