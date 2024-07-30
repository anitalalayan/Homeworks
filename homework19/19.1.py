def my_map(func, iterable: list | tuple) -> list:
    """
    Applies a given function to each item in an iterable and returns a list of the results.

    Parameters:
    - func: A function that takes a single argument and returns a value.
    - iterable: A list containing items(could be any iterable).

    Returns:
    - A list of results from applying func to each item in the iterable.

    """
    mapper = [func(item) for item in iterable]
    return mapper


def power(base: int, exponent: int) -> int:
    return base ** exponent

exponent = 3
result = my_map(lambda x:power(x, exponent), [1, 2, 3, 4, 5, 6])

print(result)


