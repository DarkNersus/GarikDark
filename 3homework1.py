# task 1

def my_div(request_1, request_2):
    try:
        request_1, request_2 = float(request_1), float(request_2)
        answer = request_1 / request_2
    except ValueError:
        return 'error', 'Ошибка числа'
    except ZeroDivisionError:
        return 'Деление на ноль!'
    return answer


my_div(input(), input())