def get_nth_element(iterable, n: int):
    it = iter(iterable)
    index = 0

    while index < n:
        try:
            next(it)
            index += 1
        except StopIteration:
            print("Index out of range")
    
    return next(it)


ls = [10, 20, 30, 40, 50]
print(get_nth_element(ls, 2))
