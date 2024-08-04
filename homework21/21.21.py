def sort_list(lst):
    return sorted(lst)

def reverse_list(lst):
    return lst[::-1]

def filter_list(lst):
    return [item for item in lst if item % 2 == 0]


def map_list(lst, func = lambda x: x ** 2):
    return [func(item) for item in lst]


list_operations = {
    'sort': sort_list,
    'reverse': reverse_list,
    'filter': filter_list,
    'map': map_list
}

def transform_list(lst, operation):
    return list_operations.get(operation)(lst)

lst = [1, 3, 2, 5, 4]

print(f"Sorted List: {transform_list(lst, 'sort')}")
print(f"Reversed List: {transform_list(lst, 'reverse')}")
print(f"Filtered List (even numbers): {transform_list(lst, 'filter')}")
print(f"Mapped List (default function): {transform_list(lst, 'map')}")

