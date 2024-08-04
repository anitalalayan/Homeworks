def make_greeting(greeting):
    def greet(name):
        print(f"{greeting}, {name}!") # or concat (+)
    return greet


user_greeting = input("Enter the greeting: ")
user_name = input("Enter the name: ")

greeting_function = make_greeting(user_greeting)
greeting_function(user_name)

