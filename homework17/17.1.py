def flatten_list(ls):
    flat_list = []
    for item in ls:
        if type(item) == list:
            flat_list += flatten_list(item)
        else:
            flat_list.append(item)
    return flat_list

ls = [1, [2, [3, 4], 5], 6, [7, 8]]
print(flatten_list(ls))
