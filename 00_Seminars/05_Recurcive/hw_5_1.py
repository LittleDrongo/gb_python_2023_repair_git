# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

# def exponentiation(a, b):
#     return (a * b)
#     return exponentiation(a, b)
    

def f(a, b):
    if (b == 1):
        return a
    if (b != 1):
        return (a * f(a, b - 1))
    
