def ascending(ls):
    if len(ls) <= 1:
        return True
    
    elif type(ls[0]) != type(ls[1]):
        return False
    
    elif ls[0] >= ls[1]:
        return False
    
    return ascending(ls[1:])


ls = [1, [2, [3, 4], 5], 6, [7, 8]]
print(ascending(ls))
