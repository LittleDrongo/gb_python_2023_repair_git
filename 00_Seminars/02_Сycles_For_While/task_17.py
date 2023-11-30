# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем стречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

array = {1, 1, 2, 0, -1, 3, 4, 4}
count = 0
for i in array:
    count += 1

print (count)

# Традиционный иттератор с функцией append




arr = [1, 1, 2, 0, -1, 3, 4, 4]

print(len(set(arr)))

#  Традиционный итератор с функцией append()
lst = []
for el in arr:
    if el not in lst:
        lst.append(el)
print(len(lst))