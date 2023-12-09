"""
    Задача №57. Решение в группах
    1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
    2. Посмотреть сколько в нем строк и столбцов
    3. Определить какой тип данных имеют столбцы
"""

from pandas import read_csv

data = read_csv('california_housing_test.csv')
# print(type(data))
# print(data.shape)
# print(data.dtypes)
# print(data.info())
print(data.describe())