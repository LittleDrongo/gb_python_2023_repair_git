# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.

# Ввод:
# 1 2 3 4 5
# Вывод:
# 0

# Ввод:
# 1 5 1 5 1
# Вывод:
# 2
# (каждое число вводится с новой строки)
# """

import random

def create_arr():
    n = int(input("Введите число N: "))
    arr = [random.randint(0, 9) for x in range(0,n)]
    print(*arr)
    return arr

arr_n = create_arr()

def search_maj():
    count = 0
    for i in range(1, len(arr_n) - 1):
#        if arr_n[i] > arr_n[i - 1] and arr_n[i] > arr_n[i + 1]:
        if arr_n[i - 1] < arr_n[i] > arr_n[i + 1]:
            count += 1
    return count

print(search_maj())