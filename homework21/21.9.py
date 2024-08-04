def make_accumlator(start=0):
    total = start
    def accumlate(arg):
        nonlocal total;
        total += arg
        return total
    return accumlate


add  = make_accumlator(10)(5)
print(add)


