"""
    Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
    Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику

    Ввод:
    values = [0, 2, 10, 6]
    if same_by(lambda x: x % 2, values):
        print(‘same’)
    else:
        print(‘different’)

    Вывод:
    same
"""
def same_by(f, lst):
    return all(f(lst[i]) == f(lst[0]) for i in range(len(lst)))


def same_by(f, lst):
    return len(set(map(f, lst))) < 2


values = [0, 2, 4, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')