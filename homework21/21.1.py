create_multiplier = lambda factor: lambda x: x * factor

multiplier_by_5 = create_multiplier(5)
result = multiplier_by_5(10)

print(result)
