def apply_twice(f, x):
    return [f(x) for _ in range(2)]


print(apply_twice(lambda y: y + 2, 10))
