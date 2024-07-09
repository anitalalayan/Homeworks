set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

union_set = set1 | set2
intersection_set = set1 & set2
symmetric_diff = set1 ^ set2

print(f"Union of set1 and set2: {union_set}")
print(f"Intersection of set1 and set2: {intersection_set}")
print(f"Symmetric difference of set1 and set2: {symmetric_diff}")


# union_set = set1.union(set2)
# intersection_set = set1.intersection(set2)
# symmetric_diff = set1.symmetric_difference(set2)
# diff = set1.difference_update(set2)
