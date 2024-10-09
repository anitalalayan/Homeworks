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
def bubble_sort(array):
    for i in range(len(array)-1):
        swapped = False

        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break

    return array


arr1 = [45, 6, 98, 23, 45, 0, 89, 3, 11]
sorted_bubble = bubble_sort(arr1)
print(sorted_bubble)
