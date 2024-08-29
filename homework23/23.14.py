#Implement a generator function custom_map(func, iterable) that mimics the behavior of the built-in map() function. It should apply func to each item in iterable and yield the results one by one. Test your function with a sample list and a lambda function that squares each element.

def custom_map(func, iterable):
    for item in iterable:
        yield func(item)
 

for num in custom_map(lambda x: x ** 2, [1, 2, 3,4,5]):
    print(num)
