def countdown_from_n(n):
    if n <= 0:
        print("Enter a non negative number.")
    else:
        for num in range(n, -1, -1):
            print(num)


n = int(input("Insert a natural number: "))
countdown_from_n(n)
