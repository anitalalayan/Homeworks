def apply_function(iterable, func):
    return [func(item) for item in iterable]

ls = [3, 67, 84, 23, 5]

print(apply_function(ls, lambda x: x * 3))
