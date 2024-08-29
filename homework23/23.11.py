#Write a generator function custom_reduce(func, iterable, initializer=None) that mimics the behavior of functools.reduce(). It should yield intermediate results of applying func cumulatively to the items of iterable, optionally starting with initializer. Test this function with a list of numbers and a lambda function that adds two numbers.


def custom_reduce(func, iterable, initializer = None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = func(value, element)
        yield value


ls = [1,2,3,4,5,6]
gen = custom_reduce(lambda x, y: x+y, ls)

for res in gen:
    print(res)
