def bar(n):
    funcs = []

    for i in range (n):
        def multiplier(x, index = i):
            print(f"Closure variables: {multiplier.__closure__}")
            return x * index
        
        funcs.append(multiplier)
    for j in funcs:
        print(f"Closures in funcs: {j.__closure__}")

    return funcs

ex = bar(3)

print(ex[0](3))
