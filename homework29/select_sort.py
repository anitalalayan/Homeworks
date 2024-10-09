import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} execution time: {end - start:.9f} seconds")
        return result
    return wrapper


@timing_decorator
def selection_sort(array):
    for i in range(len(array) - 1):
        current_min = i

        for j in range(i + 1, len(array)):
            if array[j] < array[current_min]:
                current_min = j

        array[i], array[current_min] = array[current_min], array[i]

    return array


arr2 = [56, 6, 98, 23, 45, 0, 89, 3, 11]
print(selection_sort(arr2))
