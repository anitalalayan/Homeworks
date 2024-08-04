def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

def to_title_case(s):
    return s.title()

def reverse_string(s):
    return s[::-1]

string_operations = {
    'uppercase': to_uppercase,
    'lowercase': to_lowercase,
    'titlecase': to_title_case,
    'reverse': reverse_string
}

def manipulate_string(s, operation):
    return string_operations.get(operation)(s)

user_string = input("Enter the string: ")
operation = input("Enter the operation (uppercase, lowercase, titlecase, reverse): ").strip().lower()

print(manipulate_string(user_string, operation))
