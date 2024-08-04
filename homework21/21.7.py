def sep_even_n(ls):
    result = list(filter(lambda x: x % 2 == 0, ls))
    print(result)



ls = [ 10, 45, 78, 90, 24, 1, 7, 36, 278]
print(sep_even_n(ls))
