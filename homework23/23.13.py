#Create a generator function custom_filter(func, iterable) that mimics the behavior of the built-in filter() function. It should yield items from iterable where func(item) returns True. Test this function with a list of integers and a lambda function that checks if the number is even.

def custom_filter(func, iterable):
    for item in iterable:
        if func(item):
            yield item 


for num in custom_filter(lambda x: x % 2 == 0, [1,2, 15, 16, 20, 24, 62, 5]):
    print(num)
