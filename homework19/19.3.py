def my_zip(*iterables) -> list:
    min_length = min([len(x) for x in iterables])
    res = [tuple([item[i] for item in iterables]) for i in range(min_length)]
    return res


tennis_players = ['Novak Djokovic', 'Rafa Nadal', 'Roger Federer', 'Andre Agassi'] 
titles = [ 24, 22, 20, 8, 19]

print(my_zip(tennis_players, titles))
