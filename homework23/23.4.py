#Use a generator expression to create a generator that yields the squares of numbers from 1 to 20. Iterate through this generator to print all squared values.


generator = (num ** 2 for num in range(1, 21))
for num in generator:
    print(num)
