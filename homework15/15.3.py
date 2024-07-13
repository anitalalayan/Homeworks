def list_elements(list):
    for i in list:
        print(i)


ls = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = input("Insert the elements of the list: ")
    ls.append(ele)



list_elements(ls)
