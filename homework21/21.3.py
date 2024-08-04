def apply_twice(f, x):
    return f(f(x))

def add_3(y):
    return y + 3

result = apply_twice(add_3, 7)

print(result)
