words_to_find = ["example", "all", "word", "up", "did", "him"]
word_counts = dict.fromkeys(words_to_find, 0)

myfile = open('peterrabbit.txt', 'r')

text = myfile.read()
words = text.split()

for word in words:
    if word in word_counts:
        word_counts[word] += 1

for word, count in word_counts.items():
    print(f'Word "{word}" occurs {count} times.')
