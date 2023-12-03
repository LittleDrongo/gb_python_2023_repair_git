"""
    Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
    Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
    Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

    Если строк меньше двух, выдайте текст
    ОШИБКА! Размерности таблицы должны быть больше 2!.

    Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

    print_operation_table(lambda x, y: x * y, 3, 3)
    На выходе:


    1 2 3
    2 4 6 
    3 6 9
"""
# Создание таблицы с размером 3x3, заполненной нулями
a = 3           
mas = [0] * a 
for i in range(a): 
    mas[i] = [0] * a 
# print(mas) # Выведет [[0, 0, 0], [0, 0, 0], [0, 0, 0]]     

mas2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]     
print(mas2[1][1])
 

 
# def print_operation_table(operation, num_rows=3, num_columns=3):
#     error_string = 'ОШИБКА! Размерности таблицы должны быть больше 2!'
#     if num_rows < 3 or num_columns < 3:
#         print(error_string)
#     else:
#         for i in range(1, num_rows + 1): 
#             for j in range(1, num_columns + 1):
#                 table = [ [i]*j for i in range(j)]
#                 if i == 1:
#                     table = [ [i] * j ]
#                     print(" ".join(map(str, num_rows)))

def print_operation_table(operation, rows, cols):
    # Создание таблицы
    table = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Нумерация строк и столбцов
    for i in range(1, rows + 1):
        table[i][0] = i
    for j in range(1, cols + 1):
        table[0][j] = j

    # Заполнение таблицы результатами бинарных операций
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            table[i][j] = operation(table[i][0], table[0][j])

    # Вывод таблицы
    for row in table:
        print(' '.join(map(str, row)))

# Пример использования с операцией сложения
print_operation_table(lambda x, y: x + y, 4, 4)



       

         
# def print_operation_table(operation, num_rows=3, num_columns=3):
#     error_string = 'ОШИБКА! Размерности таблицы должны быть больше 2!'
#     if num_rows < 3 or num_columns < 3:
#         print(error_string)
#     else:
            
#         for i in range(1, num_rows + 1):
#             row_values = [operation(i, j) for j in range(1, num_columns + 1)]
#             print(" ".join(map(str, row_values)))


        # # if num_rows == 1:
        # a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
        # for i in a:
        #     # print(*[f"{x:>3}" for x in i])
        #     print(*[x for x in i])

# print_operation_table(lambda x, y: x + y, 4, 4)
print()
# print_operation_table(lambda x, y: x * y, 3, 3)
print()
# # print_operation_table(lambda x, y: x - y, 5, 5)
    
# Сначала нужно создать таблицу размером 5х5 с нумеровонным первым столбцом и строкой, пример:


# 1 2 3 4 5
# 2 0 0 0 0
# 3 0 0 0 0
# 4 0 0 0 0
# 5 0 0 0 0

# А потом нужно заполнить саму таблицу результатами бинарных операций
# -------------------------------------------------

# print_operation_table(lambda x, y: x + y, 4, 4)

# Ожидаемый ответ:

# 1 2 3 4
# 2 4 5 6
# 3 5 6 7
# 4 6 7 8

# Ваш ответ:

# 2 3 4 5
# 3 4 5 6
# 4 5 6 7
# 5 6 7 8

# -------------------------------------------------

# print_operation_table(lambda x, y: x - y, 5, 5)


# Ожидаемый ответ:

# 1 2 3 4 5
# 2 0 -1 -2 -3
# 3 1 0 -1 -2
# 4 2 1 0 -1
# 5 3 2 1 0

# Ваш ответ:

# 0 -1 -2 -3 -4
# 1 0 -1 -2 -3
# 2 1 0 -1 -2
# 3 2 1 0 -1
# 4 3 2 1 0

# -------------------------------------------------

# print_operation_table(lambda x, y: x / y, 4, 4)


# Ожидаемый ответ:

# 1 2 3 4
# 2 1.0 0.6666666666666666 0.5
# 3 1.5 1.0 0.75
# 4 2.0 1.3333333333333333 1.0

# Ваш ответ:

# 1.0 0.5 0.3333333333333333 0.25
# 2.0 1.0 0.6666666666666666 0.5
# 3.0 1.5 1.0 0.75
# 4.0 2.0 1.3333333333333333 1.0

# -------------------------------------------------

# print_operation_table(lambda x, y: x * y)


# Ожидаемый ответ:



# Ваш ответ:

# 1 2 3
# 2 4 6
# 3 6 9