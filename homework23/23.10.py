#Create a generator exception_propagator(iterable) that yields each item in iterable. If an item is "error", raise a ValueError exception with the message “An error occurred!“. Test this generator with a list containing the string "error".

def exception_propagator(iterable):
    for item in iterable:
        if item == "error":
            raise ValueError("An error occured!")
        yield item 


ls = [1, 2 , 5, "error", 34]

try:
    for i in exception_propagator(ls):
        print(i)
except ValueError as e:
    print(e)
