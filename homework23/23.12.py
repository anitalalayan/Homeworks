#Develop a generator function custom_zip(*iterables) that mimics the behavior of the built-in zip() function. It should yield tuples containing items from each iterable passed as arguments, stopping when the shortest iterable is exhausted. Test your generator with two or more lists of different lengths

def custom_zip(*iterables):
    shortest_it = min(len(iterable) for iterable in iterables)
    
    for i in range(shortest_it):
        yield tuple(it[i] for it in iterables)

ls1 = [1,2,3,4,5]
ls2 = ['hello', 'bye', 'friend', 'alo']
ls3 = [23.5, 'abc', [1,2,4], 'name', 32]

gen = custom_zip(ls1, ls2, ls3)

for item in gen:
    print(item)
