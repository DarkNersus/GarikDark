#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
num_user = int(input('Введите целое положительное число: '))
cur_max = 0
num = num_user

while num > 0:
    number = num % 10
    if number > cur_max:
        cur_max = number
        if cur_max == 9:
            break
    num = num // 10
print(f'Наибольшая цифрв у введенного числа {num_user}:', cur_max)