# task 2
act = list(input("Введите текст: "))
for exc in range(2, len(act), 3):
    act[exc - 2], act[exc] = act[exc], act[exc - 2]
print(act)