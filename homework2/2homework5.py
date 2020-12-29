# task 5
my_list = [7, 5, 3, 3, 2]
request = input('Введите число: ')
for index, num in enumerate(my_list):
    if int(request) < int(num):
        continue
    my_list.insert(index, request)
    break
else:
    my_list.append(request)
print(my_list)