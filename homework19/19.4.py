def iteration(list):
    it = iter(list)
    while True:
        try:
            item = next(it)
            print(item)
        except StopIteration:
            print("End of Iteration")
            break


ls = [23, -45, 78, 289, 35, 0, 57]

iteration(ls)
