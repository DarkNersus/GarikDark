# task 4
strings = input('Введите несколько слов: ')
word = strings.split()
for txt, words in enumerate(word, start=1):
    print(txt, words[:10])
