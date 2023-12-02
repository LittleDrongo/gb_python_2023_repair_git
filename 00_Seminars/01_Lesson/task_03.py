# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

sum = 0
classes = 3

for i in range(classes):
    count = int(input(f"Введите количество учащихся в {i+1}-м классе: "))
    even = count % 2
    count = count + even
    sum = sum + count

print(sum / 2)