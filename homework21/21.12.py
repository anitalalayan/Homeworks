def make_memoize(f):
    cache = {}
    
    def memoized_function(*args):
        return cache.get(args)
    return memoized_function

def foo(x):
    return x * x

memoized_foo = make_memoize(foo)

print(memoized_foo(4))
print(memoized_foo(4))
