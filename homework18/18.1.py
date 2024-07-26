def greet_user(first_name, last_name, greeting_message = "Hello,"):
    return f"{greeting_message} {first_name} {last_name}"


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
custom_greeting = input("Pass a greeting message (optional): ")


if custom_greeting.strip():
    print(greet_user(first_name, last_name, custom_greeting))
else:
    print(greet_user(first_name, last_name))


