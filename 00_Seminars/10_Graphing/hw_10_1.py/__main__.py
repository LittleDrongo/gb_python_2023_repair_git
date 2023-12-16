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


def decode_via_dummies(data):
    """
    Метод на вход принимат DataFrame и возвращает данные в кодировке 'One not' с таблицей бинароного вида (int) \n
    В качестве основного метода используется get_dummies
    """
    bin_data = pd.get_dummies(data, dtype=int)
    return bin_data


def decode_to_one_hote(data):
    """
    Метод на вход принимат DataFrame и возвращает данные в кодировке 'One not' с таблицей бинароного вида (int) \n
    """

    # Получаю список уникальных значений
    data_unique = data['whoAmI'].unique() 

    # Создают наименование столбцов для последующего создания таблицы
    data_unique_header = []
    for i in data_unique:
        data_unique_header.append(f'whoAmI_{i}')

    # Получаем кол-во строк таблицы
    lengh_table = len(data.axes[0])

    # Получаем кол-во строк стобцов
    columns_count = len(data_unique)

    # Создаю новую таблицу типа OneHot пока с пустыми значениями

    df = pd.DataFrame()

    for i in data_unique:
        df.insert (loc= len(df.columns) , column=i, value=None)

    for j in data_unique:    
        for i in range(lengh_table):    
            df.at [i, j] = 0

    # Заполняем столбец значением 1 если оно равно заголовку в Data
    for i in data_unique:
        df.loc[data['whoAmI'] == i, i] = int(1)

    # Переименовываем столбцы в корректное название
    for i in range(columns_count):
        df.rename(columns = {data_unique[i] : data_unique_header[i]}, inplace = True)

    return df


# Вызов методов

res_data_1 = decode_via_dummies(data)
print(type(res_data_1))
print(res_data_1)


res_data_2 = decode_to_one_hote(data)
print(type(res_data_2))
print(res_data_2)


print(
    res_data_1.equals(res_data_2)
    )


"""
Резюме, по какой то причине если сравнить таблицы данных на сходство через 'equals' мой вариант функции и встроенный вариант get_dummy имеет некую разницу, однако я не смог понять что не так.
"""