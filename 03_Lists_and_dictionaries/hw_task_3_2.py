# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

list_1 = [1, 2, 6, 4, 3]
k = 6

def find_nearest(arr, target):
    relust = float('inf')
    for num in arr:
            diff = abs(num - target)
            if diff < abs(relust - target):
                relust = num
    return relust

print( 
     find_nearest(list_1, k)
)