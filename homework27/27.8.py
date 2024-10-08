
class PasswordValidator:
    def __init__(self, min_length):
        self.min_length = min_length

    def __set__(self, instance, value):
        if len(value) < self.min_length:
            raise ValueError(f"Password must be at least {self.min_length} characters long.")

        digits = '0123456789'

        found_digit = False
        for digit in digits:
            if digit in value:
                found_digit = True
                break

        if not found_digit:
            raise ValueError("Password must contain at least one number.")

        instance.__password = value

    def __get__(self, instance, owner):
        return instance.__password


class Account:
    password = PasswordValidator(min_length=8)



account = Account()
account.password = "barevvvvvvv"
print(account.password)
