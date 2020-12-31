# task 2

def personal_info(**inf):
    return inf


print(personal_info(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    bitrhday=input('год рождения: '),
    city=input('город проживания: '),
    email=input('email: '),
    phone=input('Телефон: '),
))