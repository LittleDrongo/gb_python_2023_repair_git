# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

array = [0, -1, 5, 2, 3]
count = 0

print(len(array))

# for item in arr
for i in range(1, 5): #len(array)): # i пробегает значения в диапазоне от 1 до 5 не включая 5.
    if array[i] > array[i - 1]:
        count += 1

# Автор Лутц





