# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Пример

# На входе:



a1 = 2
d = 3
n = 4

def fill_elements_Of_arithmetic_progression(a1, d, n):
    for i in range(n):
        print(a1 + i * d)

fill_elements_Of_arithmetic_progression(a1, d, n)