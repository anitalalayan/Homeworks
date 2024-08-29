def prime_generator(n):
    if n <= 1:
        yield False

    for number in range(2, n):
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number



gen_prime = prime_generator(100)

for ele in gen_prime:
    print(ele)
