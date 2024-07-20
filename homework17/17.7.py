def ispower_of_2(n):
    if n <= 0:
        return False 
    while n != 1:
        if n % 2!= 0:
            return False
        n = n // 2
    return True 



n = int(input("Insert a number: "))

print(ispower_of_2(n))
