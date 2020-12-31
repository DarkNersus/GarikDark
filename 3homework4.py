# task 4

# def my_func_1(x, z):
#    try:
#        ans = x ** z
#   except TypeError:
#        return 'Enter float'
#    return ans


# print(my_func_1(20, -2))


# второй вариант
def my_func(x, z):
    try:
        x, z = float(x), int(z)
        res = x
        for i in range(abs(z) - 1):
            res = res * x
        return 1 / res
    except ValueError:
        return 'Check value'

print(my_func(20, -2))




