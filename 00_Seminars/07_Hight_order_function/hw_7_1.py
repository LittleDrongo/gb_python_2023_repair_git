"""
    Напишите функцию print_operation_table(operation, num_num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
    Аргументы num_num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
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

def print_operation_table(operation, num_rows, num_columns):

    error_string = 'ОШИБКА! Размерности таблицы должны быть больше 2!'
    if num_rows < 3 or num_columns < 3:
        print(error_string)
    else:
        table = [[1] * (num_columns) for _ in range(num_rows)]

        for i in range(1, num_rows):
            table[i][0] = i + 1
        for j in range(1, num_columns):
            table[0][j] = j + 1
    
        for i in range(1, num_rows):
            for j in range(1, num_columns):
                table[i][j] = operation(table[i][0], table[0][j])

        for row in table:
            print(' '.join(map(str, row)))

# -------------------------------------------------

print_operation_table(lambda x, y: x + y, 4, 4)

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