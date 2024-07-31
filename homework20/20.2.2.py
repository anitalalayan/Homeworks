def make_counter():
    counter = 0
    def count():
        nonlocal counter;
        counter += 1
        return counter
    return count

res = make_counter()


print(res())
print(res())
print(res())
