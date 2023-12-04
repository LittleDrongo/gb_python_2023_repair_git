"""
    Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.

    Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
    Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
    Фразы отделяются друг от друга пробелами.

    Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
    Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

    Пример

    На входе:


    stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
    На выходе:


    Парам пам-пам
"""
from math import *

# Парам   пам-пам
# Фраза   Фраза
#         слова

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'


stroka2 = 'пара-ра-рам рам-пам-папам па-ра-па-дама'


stroka3 = 'пара-ра-рам-рам-пам-апам-па-ра-па-дам'

 

def vowel_counts(string): # Считает кол-во гласных букв
    vowel_letters = 'АИОУЫЭЕЁЮЯ' # Гласные буквы
    count = 0
    string = string.upper()
    for char in string:
        if char in vowel_letters:
            count += 1
    return count

def consonant_counts(string): # Считает кол-во согласных букв
    consonant_letters = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ' # Согласные буквы
    count = 0
    string = string.upper()
    for char in string:
        if char in consonant_letters:
            count += 1
    return count

def phrases_counts(string):
    count = 0
    phrases = string.split(' ')
    for i in phrases:
        count += 1
    return count

def check_for_rhythm(poem):
    str = poem.split()
    count_arr = []
    count = -1
    for phrase in str:
        count += 1
        count_arr.append(vowel_counts(phrase))
        count_arr_set = set(count_arr)

    if count == 0:
        return 0
    else: 
        return (len(count_arr_set)) 




def check_param_pam_pam(str):
    okay_string = 'Парам пам-пам'
    not_okay_string = 'Пам парам'
    error_string = 'Количество фраз должно быть больше одной!'

    if check_for_rhythm(str) == 1:
        print(okay_string)

    if check_for_rhythm(str) == 0:
        print(error_string)

    if check_for_rhythm(str) > 1:
        print(not_okay_string)


check_param_pam_pam(stroka)


check_param_pam_pam(stroka2)

check_param_pam_pam(stroka3)

# print(check_param_pam_pam(stroka)
#     )
# написать функцию которая будет отвечать строками 
# если 1 - хорошо
# если 0 - ошибка
# если >1 - не хорошо


# # Если фраза только одна, то ритм определить не получится и необходимо вывести:
# phrases = 0
# if phrases < 2:
#     print(error_string)
# else:
#     print(2)


    #  Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
    # Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
    # Фразы отделяются друг от друга пробелами.