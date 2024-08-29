def fibonacci_generator(n):
    x_2 = 0
    x_1 = 1

    yield x_2
    yield x_1

    for x in range(2, n + 1):
        yield x_2 + x_1
        x_2, x_1 = x_1, (x_2 + x_1)



gen_fib = fibonacci_generator(6)

print(next(gen_fib))

for item in gen_fib:
    print(item)
