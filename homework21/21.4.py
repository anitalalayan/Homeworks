def add_with_five(x):
    return x + 5

def mul_with_two(y):
    return y * 2

def compose(f,g):
    return lambda x: f(g(x))

res = compose(add_with_five, mul_with_two)

print(res(4))
