from module_one import *
# import module_one
# import module_one as m1

# print(module_one.max1(5,9))

print(max1(5,9))

def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa


print(sum_numbers(10))


def sum_numbers(n = 10): #Аргумент с значением по умолчанию 10
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa


print(sum_numbers(10))


def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(
    sum_str('321','2321','321321')
)
