"""
    Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
    Ваша задача перевести его в one hot вид. 
    
    Сможете ли вы это сделать без get_dummies?

    import random
    lst = ['robot'] * 10
    lst += ['human'] * 10
    random.shuffle(lst)
    data = pd.DataFrame({'whoAmI':lst})
    data.head()
"""

import random
import pandas as pd

# Кодировка категорий
# Компьютер не понимает человеческую речь. Слова "кошка", "собака" для него ничего не значат. 
# Но компьютер понимает числа. Как же мы можем заменить имя числом? 
# В данном случае нам поможет one hot кодировка. В которой присутствие значения обозначается 1, а отсутствие 0.

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

print(data)

def decode_to_one_hote(data):
    """Функция на вход принимат DataFrame и возвращает данные в кодировке 'One not' с таблицей бинароного вида (int)"""
    bin_data = pd.get_dummies(data, dtype=int)
    return bin_data

# oh_data2 = decode_to_one_hote(data)
# print(oh_data2)

# Получаю список уникальных значений
data_unique = data['whoAmI'].unique() 
print(sorted(data_unique))


# Создают наименование столбцов для последующего создания таблицы
data_unique_header = []
for i in data_unique:
    data_unique_header.append(f'whoAmI_{i}')


# Получаем кол-во строк таблицы
lengh_table = len(data.axes[0]) 


# Создаю новую таблицу типа OneHot пока с пустыми значениями

df = pd.DataFrame()

for i in data_unique:
    df.insert (loc= len(df.columns) , column=i, value=None)

for j in data_unique:    
    for i in range(lengh_table):    
        df.at [i, j] = 0

print('это пустая таблица с 0')
print(df)

# #Заполняем столбец значением 1 если оно равно заголовку в Data
df.loc[data['whoAmI'] == 'robot', 'robot'] = 1


#Заполняем столбец значением 1 если оно равно заголовку в Data
for i in data_unique:
    df.loc[data['whoAmI'] == i, i] = 1


#

print()
print(df)

# data_list = list(data)

# print(data)
# for j in data_unique:    
#     for i in range(lengh_table):    
#         df.at [i, j] = 0

# # print(data)
# for i in data_unique:
#     for j in range(lengh_table):    
#         df.at [j, data_unique[i]] = 54

print(df)
    
# data.loc[data['whoAmI'] == 'robot', 'whoAmI'] = 0 # ВОТ ЭТО ПОНАДОБИТЬСЯ ЧТОБЫ ПЕРЕИМЕНОВАТЬ В 1 и 0

    # res = data.iloc[:, :]
    # print(temp)
    # df.at [i, 'robot'] = 54

# temp.loc[((df['col1'] == 'A') &(df['col2' ] == 'G'))]
# print(df)

"""for i in lengh_table:
    yachika = df[data_unique[0]]. values [i]
    print(yachika)
"""
# print(df)




# df2 = pd.DataFrame()

# df2.at [1, 'robot'] = 54
# print(df)

# for uniq in data_unique:
#     for pos in lengh_table:
#         df.at [pos, uniq] = '99'



# oh_data = pd.DataFrame({'whoAmI':lst})
# oh_data.head()
# print(res)

# print(type(data))         # тип данных всего объекта
# print(data.shape)         # размер матрицы (строки, столбцы)
# print(data.dtypes)        # тип данных
# print(data.info())        # информация
# print(data.describe())    # прочее



# print(data)