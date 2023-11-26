#    Тип коллекции	Изменяемость	Индексированность	Уникальность	Как создаём	    Функция
#    Список	        +	            +	                -	            []	            list()
#    Кортеж	        -	            +	                -	            (,)	            tuple()
#    Строка	        -	            +	                -	            ""	            str()
#    Множество	    +	            -	                +	            {}	            set()
#    Замороженное   -               -   	            +		                        frozenset()
#    Словарь	    +э, -к, + з	    -	                +э, +к, -з	    {key: value,}	dict()


# Списки
list_1 = []                 # Создание пустого списка
list_1 = list()             # Создание пустого списка, через функцию
list_1 = [1, 2, 3, 8]       # Создание пустого списка заполненого

print(list_1)               # Вывести список
print(*list_1)              # * Убрать скобочки
       
for i in list_1:            #Пример взаимодействия цикла с списком
    print(i)

list_1.append(9)            # Добавить значения в список список

list_1.pop()                # Удалить последний элемент при этом может вернуть элемент.
list_1.pop(0)               # Удалить элемент 0 индекса
list_1_pop = list_1.pop()   # При этом может вернуть элемент.

list_1.insert(2, 11)        # На позицию 2 вставить элемент 11

# ------------------------------

# Срез списка

# ------------------------------


# Кортежи

tuple_1 = ()                # Создание пустого кортежа
tuple_1 = (1,)              # Создание заполненного кортежа в конце оставить запятую

v = [1, 8, 9]               # Создание списка
v = tuple(v)                # Преобразования списка в кортеж


a, b, c = v                 # Распаковка кортежа
print(a,b,c)


tuple_2 = (1, 2, 3, 5, )
for i in tuple_2:
    print(i)

# ------------------------------

# Словари
    
dict = {}                                   # Создание пустого словаря
dict['q'] = 'qwerty'
dict['w'] = 'werty'
print(dict['q'])


dictionary = {'first_name': 'Алексей',
              'second_name': 'Фомин',
              'b_day': '04.10.1988'
              }

print (dictionary['first_name'])

del dictionary['first_name']                #Удаление ключа

for item in dictionary:
    print(item)

print(dictionary.items())

# ------------------------------

# Множества

colors = {'red', 'green', 'blue'}
colors.add('grey')
colors.remove('grey')                       # Удаляет и завершает програму ошибкой

colors.discard('red')                       # Удаляет и пропускает строку без ошибки
colors.clear()

a_set = {1, 2, 3, 4, 5}
b_set = {4, 5, 6, 7, 8}
c_set = a_set.copy()

u_set = a_set.union(b_set)                   # Объеденение
i_set = a_set.intersection(b_set)            # Пересечение
dif_set = a_set.difference(b_set)            # Разница

f_set = frozenset(a_set)                     # Замороженное множество

# ------------------------------


# List Comprehension

# ------------------------------

# Профилирование и отладка
# ------------------------------



