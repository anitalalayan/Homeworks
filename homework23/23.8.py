#Use a generator expression to filter and yield only even numbers from a list of numbers. Test this generator with a list of integers from 1 to 50.

gen = (x for x in range(1, 50) if x % 2 == 0)


for num in gen:
    print(num)
