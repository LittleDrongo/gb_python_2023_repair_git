"""
    Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
    Используйте модуль pandas.
"""
import os

from pandas import * # http://pandas.geekwriter.ru/getting_started/index.html

data = read_csv('california_housing_train.csv')

interim_data = data[(data['population'] >= 0) & (data['population'] < 500)] 
sum_data = interim_data['median_house_value'].sum() 
cnt_data = interim_data['median_house_value'].count()

avg = sum_data / cnt_data


# Среднее арифметическое = сумма всех значений / общее количество значений.

# print(type(data))         # тип данных всего объекта
# print()
# print(data.shape)         # размер матрицы (строки, столбцы)
# print()
# print(data.dtypes)        # тип данных
# print()
# print(data.info())        # информация
# print()
# print(data.describe())    # прочее