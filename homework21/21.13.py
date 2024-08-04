def bar(n):
    functions = []
    
    for i in range(n):
        def multiplier(x, i=i):
            return x * i
        functions.append(multiplier)

    
    for func in functions:
        closure = func.__closure__
        print(f"Function __closure__: {closure}")
        
    return functions

print(bar(5))
