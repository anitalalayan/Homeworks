def make_multiplier_of(n):
    def multiplier(number):
        return n * number
    return multiplier



product = make_multiplier_of(4)
print(product(5))

product1 = make_multiplier_of(10)
print(product1(30))
