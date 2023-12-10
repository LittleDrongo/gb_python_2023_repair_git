"""
    Дан файл california_housing_train.csv.
    Найти максимальное значение переменной "households" в зоне минимального значения переменной "population" и сохраните это значение в переменную max_households_in_min_population.
    Используйте модуль pandas.
"""

#   longitude  latitude  housing_median_age total_rooms  total_bedrooms  population   median_income  median_house_value  households

from pandas import * # http://pandas.geekwriter.ru/getting_started/index.html

data = read_csv('california_housing_train.csv')
max_households_in_min_population = data[data['population'] == data['population'].min()].households.max()
print(max_households_in_min_population)