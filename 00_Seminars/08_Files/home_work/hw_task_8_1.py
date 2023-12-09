
from os.path import exists
from csv import DictReader, DictWriter

file_name = 'phone.csv'
export_file_name = 'copy_phone.csv'

class MenuTextColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = "\033[0m"   


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    is_valid_name = False
    while not is_valid_name:
        try:
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise NameError('Не валидное имя')
            else:
                is_valid_name = True
        except NameError as err:
            print(err)
            continue

    is_valid_second_name = False
    while not is_valid_second_name:
        try:
            last_name = input('Введите фамилию: ')
            if len(last_name) < 2:
                raise NameError('Не валидная фамилия')
            else:
                is_valid_second_name = True
        except NameError as err:
            print(err)
            continue
    
    is_valid_phone = False
    while not is_valid_phone:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Не вверная длина номера')
            else:
                is_valid_phone = True
            
        except ValueError:
            print('Не валидный номер')
            continue
            
        except LenNumberError as err:
            print(err)
            continue
           
    return [first_name, last_name, phone_number]


def create_file(file_name):
    # Менеджер контекта
    with open(file_name, 'w', encoding='utf-8') as data:                            
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name, lst):
    res = read_file(file_name)
    for elem in res:
        if elem['Телефон'] == str(lst[2]):
            print('Такой телефон уже существует')
            return

    obj = {'Имя': lst[0], 'Фамилия': lst[1], 'Телефон': lst[2]}
    res.append(obj)

    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def read_line(file_name, line):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)[line - 1]

def count_lines(file_name):
    elems = 0
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        for i in f_reader:
            elems += 1            
        return elems

def print_lines(file_name):

    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        num = 1
        for i in f_reader:
            print(num, i)
            num += 1


def show_menu():
    print()
    print(f'{MenuTextColor.YELLOW}МЕНЮ ВЫБОРА {MenuTextColor.RESET}')
    print('1. Показать еще раз меню')
    print('2. Показать записи справочника')
    print('3. Внести запись в справочник')
    print('-----------------------------')
    print('4. Показать пронумерованный список записей в справочнике')
    print('5. Скопировать запись из справочника')
    print('0. Завершить работу')
    print()



def main():
    show_menu()
    while True:
        command = input('Введите команду: ')
        if command == '0':
            print(f'{MenuTextColor.OKCYAN}Завершаем работу{MenuTextColor.RESET}')
            break
        elif command == '1':
            show_menu()
        elif command == '2':
             if not exists(file_name):
                 print(f'Файл {file_name} отсутствует, создайте его')
                 continue
             print(read_file(file_name))
        elif command == '3':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == '4':
            print_lines(file_name)
        elif command == '5':
            is_valid_line = False
            while not is_valid_line:
                max_line = count_lines(file_name)         
                line = int(input('Введите номер строки для копирования: '))
                if line <= max_line:
                    print(f'{MenuTextColor.OKCYAN}Запись скопирована успешно!{MenuTextColor.RESET}')
                    print(read_line(file_name, line))
                    is_valid_line = True
                else:
                    print(f"{MenuTextColor.FAIL}Внимание, такой строки в справочнике нет, всего в словаре {max_line} записей.{MenuTextColor.RESET}")

        else:
            print(f'{MenuTextColor.FAIL}Внимание, не правильная команда!{MenuTextColor.RESET}')

main()