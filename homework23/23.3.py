#Implement an infinite generator function infinite_sequence() that yields numbers starting from 1 and increments by 1 indefinitely. Use next() to retrieve and print the first 10 numbers from this generator.

def infinite_sequence():
    num = 1
    while True:
        yield num
        num += 1


gen = infinite_sequence()

for _ in range(10):
    print(next(gen))
