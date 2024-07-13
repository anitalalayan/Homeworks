def digits_sum(number):

    digit_sum = 0

    while number > 0:
        digit  = number % 10
        number = number // 10
        digit_sum += digit

    return(digit_sum)

number = int(input("Insert a number: "))
print(digits_sum(number))
