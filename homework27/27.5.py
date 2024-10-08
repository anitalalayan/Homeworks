class ValidatedString:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Must be a string.")
        if len(value) < self.min_length:
            raise ValueError(f"String must be at least {self.min_length} characters long.")
        instance.__name = value

    def __get__(self, instance, owner):
        return instance.__name

class User:
    username = ValidatedString(6)
    def __init__(self, name):
        self.name = name


user = User("Alice")
user.username = "al"

print(user.username)

