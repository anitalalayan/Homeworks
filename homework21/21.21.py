def sort_list(lst):
    return sorted(lst)

def reverse_list(lst):
    return lst[::-1]

def filter_list(lst, condition):
    return [item for item in lst if condition(item)]

def map_list(lst, function):
    return [function(item) for item in lst]


list_transformations = {
    'sort': sort_list,
    'reverse': reverse_list,
    'filter': filter_list,
    'map': map_list
}

def transform_list(lst, operation, *args):
    return list_transformations.get(operation)(lst, *args)

print(transform_list([5, 3, 9, 1], 'sort'))
print(transform_list([5, 3, 9, 1], 'reverse'))
print(transform_list([1, 2, 3, 4, 5], 'filter', lambda x: x % 2 == 0))
print(transform_list([1, 2, 3, 4, 5], 'map', lambda x: x * 2))
