def compose(f, g):
    return lambda x: f(g(x))


def square(x):
    return x * x

def increment(x):
    return x + 1

composed_function = compose(square, increment)

result = composed_function(4)

print(result)
