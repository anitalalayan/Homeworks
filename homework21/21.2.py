def make_adder(n):
    return lambda x: x + n

add_10 = make_adder(10)
result = add_10(23)

print(result)
