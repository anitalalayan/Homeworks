def maximum(a, b, c): 

    if (a >= b) and (a >= c): 
        maximum = a 

    elif (b >= a) and (b >= c): 
        maximum = b 
    else: 
        maximum = c 
        
    return maximum

 
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
c = int(input("Enter the third number (c): "))
    

print(f"The max number is {maximum(a, b, c)}.") 
