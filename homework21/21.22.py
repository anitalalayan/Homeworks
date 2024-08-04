def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def square_root(number):
    if number < 0:
        return "Cannot compute square root of a negative number."
    return number ** 0.5

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


math_functions = {
    'square': square,
    'cube': cube,
    'square_root': square_root,
    'factorial': factorial
}

def math_operations(number, operation):
    return math_functions.get(operation)(number)


print(math_operations(5, 'square'))        
print(math_operations(2, 'cube'))       
print(math_operations(25, 'square_root'))  
print(math_operations(4, 'factorial'))    
