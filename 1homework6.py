#6.
while True:
    day = 0
    start_km = int(input('Стартовый результат: '))
    last_km = int(input('Финальный результат: '))
    if start_km > last_km or not(start_km > 0):
        print('Введены неверные данные')
    else:
        while start_km < last_km:
            start_km *= 1.1
            day += 1
        print(f'Спортсмен добьеться результатов за {day} дней')