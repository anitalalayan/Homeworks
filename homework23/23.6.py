#Create a generator function repeat_element(element, times) that yields the given element a specified number of times. Test this generator with different inputs.


def repeat_element(element, times):
    for _ in range(times):
        yield element 


gen = repeat_element('hello', 4)

for i in gen:
    print(i)
