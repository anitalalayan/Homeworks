def power_factory(n):
    def power(base):
        return base ** n
    return power

res = power_factory(5)(2)

print(res)
