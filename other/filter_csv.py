import csv

def filter_csv(csv_file, conditions):
    # Открываем файл CSV для чтения
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        # Создаем объект csv.reader
        reader = csv.reader(file)

        # Читаем заголовок
        header = next(reader)

        # Получаем индексы колонок из условий
        indices = {key: header.index(key) for key in conditions.keys()}
        
        # Создаём результирующий массив строк
        result = []

        # Добавляем заголовок
        result.append(','.join(header))

        # Добавляем строки и фильтруем по условиям
        for row in reader:
            if all(row[indices[key]] == value for key, value in conditions.items()):
                # print(','.join(row))
                result.append(','.join(row))

        return result


# Пример использования функции
conditions = {'type': '2-й', 'traectory': 'Морт'}
csv_file = 'mort.csv'
res1 = filter_csv(csv_file, conditions)

for i in res1:
    for j in res1:
        print(i)
    # print(i)