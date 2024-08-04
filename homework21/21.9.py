def make_accumulator(start=0):
    total = start
    
    def accumulator(value):
        nonlocal total
        total += value
        return total
    
    return accumulator

accum = make_accumulator(15)
print(accum(5))   
print(accum(3))
