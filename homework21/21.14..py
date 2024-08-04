def add(x: int, y: int)->int:
    return x + y

def sub(x: int, y: int)->int:
    return x - y

def mul(x: int, y: int)->int:
    return x * y

def div(x: int, y: int)->int:
    if y == 0:
        raise ZeroDivisionError("Hey bro you can't divide by zero")
    return x // y

calculator = {'+': add, '-': sub, '*': mul, '/': div}

operator = input("Enter an operator: ")
operand1 = float(input("Enter a value for the first operand: "))
operand2 = float(input("Enter a value for the second operand: "))

def calculate(operand1, operand2, operator):
    return calculator.get(operator)(operand1, operand2)
   

print(calculate(operand1, operand2, operator))
