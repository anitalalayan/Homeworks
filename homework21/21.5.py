def power_factory(n):
    def power(x):
        return x ** n
    return power


print(power_factory(5)(3))
