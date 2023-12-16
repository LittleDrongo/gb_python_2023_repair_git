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

# print(data)

def decode_to_one_hote(data):
    """Функция на вход принимат DataFrame и возвращает данные в кодировке 'One not' с таблицей бинароного вида (int)"""
    bin_data = pd.get_dummies(data, dtype=int)
    return bin_data

oh_data2 = decode_to_one_hote(data)
print(oh_data2)

# res = data[(data[1])]
# res = data.iloc[:0, :]          #получение 2-х стлбцов через срезы, 1: - все строки; 2: - только первые 2 слобца

# Получаю список уникальных значений
data_unique = data['whoAmI'].unique() 
print(sorted(data_unique))

# Создают наименование столбцов для последующего создания таблицы
data_unique_header = []
for i in data_unique:
    data_unique_header.append([f'whoAmI_{i}'])

# Создаю новую таблицу типа OneHot пока с пустыми значениями
df = pd.DataFrame()
for i in data_unique:
    df.insert (loc= len(df.columns) , column=i, value=None)

# Получаем кол-во строк таблицы
lengh_table = len(data.axes[0]) 

df.at [1, 'robot'] = 54

# for uniq in data_unique:
#     for pos in lengh_table:
#         df.at [pos, uniq] = '99'

# print(lengh_table)
# df = pd.DataFrame(np.insert(df.values , 0, values=['A', 3, 4], axis= 0 ))

print(data_unique_header)
print(df)


# df = pd.DataFrame({'whoAmI_{i}':[1,1,3,2,6,2,8]}) # пример как заполнять таблицы и значения




# oh_data = pd.DataFrame({'whoAmI':lst})
# oh_data.head()
# print(res)

# print(type(data))         # тип данных всего объекта
# print(data.shape)         # размер матрицы (строки, столбцы)
# print(data.dtypes)        # тип данных
# print(data.info())        # информация
# print(data.describe())    # прочее



# print(data)