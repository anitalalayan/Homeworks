def make_adder(n):
    def addition(num):
        return n + num
    return addition


res = make_adder(6)(4)
print(res)
