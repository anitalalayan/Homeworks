def count_upto_n(n):
    if n <= 0:
        print("Enter a non negative number. ")
    else:
        for num in range(0, n + 1):
            print(num)


n = int(input("Enter a natural number: "))
count_upto_n(n)
