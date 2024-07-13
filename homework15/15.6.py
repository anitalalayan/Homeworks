def max_min(list):
    max_num = list[0]
    min_num = list[0]

    for num in list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return (max_num, min_num)


ls = []
n = int(input("Enter number of elements: "))
for i in range(0, n):
    ele = input("Insert the elements of the list: ")
    ls.append(ele)

max_val, min_val = max_min(ls)

print(f"Maximum value is: {max_val}")
print(f"Minimum value is: {min_val}")
