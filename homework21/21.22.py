def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def square_root(number):
    return number ** 0.5

def factorial(number):
    if number <= 1:
        return 1
    return number * factorial(number - 1)

math_functions = {
    'square': square,
    'cube': cube,
    'square_root': square_root,
    'factorial': factorial
}


def math_operations(number, operation):
    return math_functions.get(operation)(number)

num = int(input("Enter a number: "))

print(f"Square of {num}: {math_operations(num, 'square')}")
print(f"Cube of {num}: {math_operations(num, 'cube')}")
print(f"Square root of {num}: {math_operations(num, 'square_root')}")
print(f"Factorial of {num}: {math_operations(num, 'factorial')}")
