def make_memoize(f):
    cache = {}
    def memoized_function(*args):
        return cache.get(args)
    return memoized_function


def foo(x):
    return x * x

print(make_memoize(foo)(4))
print(make_memoize(foo)(4))
