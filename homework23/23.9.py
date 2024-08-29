#Create two generators: gen1() yields numbers from 1 to 5, and gen2() uses yield from to yield all values from gen1() and then yields numbers from 6 to 10. Print all values yielded by gen2().

def gen1():
    for i in range(1,6):
        yield i

def gen2():
    yield from gen1()
    for j in range(6, 11):
        yield j 



for ele in gen2():
    print(ele)
