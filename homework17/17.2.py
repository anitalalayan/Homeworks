def sum(ls):
    accumlator = 0
    for item in ls:
        if type(item) == list:
            accumlator += sum(item)

        elif type(item) == int or type(item) == float:
            accumlator += item

    return accumlator


ls = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sum(ls))
