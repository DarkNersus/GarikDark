# task 5

def summary():
    tx = False
    result = 0
    while tx == False:
        numbers = input('Введите цифры или q для выхода: ').split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                tx = True
                break
            res_line += int(num)
        result += res_line
    return result