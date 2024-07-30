def my_filter(func, iterable: list | tuple) -> list:
    """
    Filters elements of the iterable based on the provided function.

    Args:
    A function that takes a single argument and returns a boolean value.
    The iterable (list or tuple) whose elements are to be filtered.

    Returns a list containing elements of the iterable.
    """
    return [item for item in iterable if func(item)]


def evenodd(n: int) -> bool:
    """Function to check if the number is even or odd"""

    return n % 2 == 0

result = my_filter(evenodd, range(15))

print(result)
