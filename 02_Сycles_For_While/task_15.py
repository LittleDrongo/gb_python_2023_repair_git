# """
# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
# """

from random import randint

# num_watermelons = int(input('Введите кол-во арбузов: '))
watermelons_weight = list(map(int, '5 1 6 5 9'.split()))
print(max(watermelons_weight), min(watermelons_weight))



# print (max_weight)


# watermelons_weight = [randint(1, 10) for _ in range(num_watermelons)]
# можно сделать генератор списка случайных чисел, для масс арбузов.

# if watermelons_weight:
#     min_weight = max_weight = watermelons_weight[0]

#     for i in range(1, num_watermelons):
#         if watermelons_weight[i] < min_weight:
#             min_weight = watermelons_weight[i]
#         elif watermelons_weight[i] > max_weight:
#             max_weight = watermelons_weight[i]

#     print(f'Для тёщи: {min_weight} кг.\nДля себя: {max_weight} кг.')
# else:
#     print('Список масс арбузов пуст!')


