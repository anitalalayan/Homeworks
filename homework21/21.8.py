def make_greeting(greeting):
    def greet(name):
        if not isinstance(name, str):
            raise ValueError("The name must be a string")
        return f"{greeting}, {name}"
    return greet


greeting = input("Enter your greeting: ")
name = input("Enter a name: ")

#print(make_greeting(greeting)(name))


ls = ['h', 'e', 'l']

print(" ".join([greeting, name]))
