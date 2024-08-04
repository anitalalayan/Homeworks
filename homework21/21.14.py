def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculate(operand1, operand2, operator):
    return operations.get(operator)(operand1, operand2)


operand1 = float(input("Enter the first operand: "))
operand2 = float(input("Enter the second operand: "))
operator = input("Enter the operator (+, -, *, /): ")

result = calculate(operand1, operand2, operator)
print(result)
