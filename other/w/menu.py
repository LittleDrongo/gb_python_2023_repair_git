from exctractor import *
from highlighter import *
from parser_funcs import *



def main():
    
    default_find_files = []  # Список файлов для поиска
    files_from_txt = []
    
    # НАСТРОЙКИ ДЛЯ ТЕСТОВ
    default_txt = 'C:/Test/file_list.txt'
    default_start_directory = 'C:/Test/start_dr'
    default_output_directory = 'C:/Test/outpute_dir'

    # # НАСТРОЙКИ ДЛЯ СЕРВЕРА UNIX
    # default_txt = '.file_list.txt'
    # default_start_directory = '/backup/clr/tap/'
    # default_output_directory = '/backup/clr/tmp/fomin_temp/'

    YELLOW = "\033[33m"
    RESET = "\033[0m"   
    # while True:

    def show_settings():
        print("")
        print(f'{YELLOW}ПАРАМЕТРЫ РАСПАКОВЩИКА{RESET}')      
        print(f'Файл txt: {default_txt}')
        print(f'Папка поиска: {default_start_directory}')
        print(f'Папка распаковки: {default_output_directory}')
        print(f'Список файлов из txt: {pars_tapfiles_txt(default_txt)}')
        print(f'Список файлов для ручного поиска: {default_find_files}')

    def show_menu():
        print("")
        print(f'{YELLOW}МЕНЮ РАСПАКОВЩИКА TAP ФАЙЛОВ{RESET}')
        print('1. Быстрый поиск (через файл txt)')
        print('2. Ручной поиск (через консоль)')
        print('--------------------------')
        print('3. Показать меню')
        print('4. Показать настройки')
        print('--------------------------')
        print('5. Изменить список файлов')
        print('6. Изменить папку поиска')
        print('7. Изменить папку распаковки')
        print('--------------------------')
        print('9. Показать файлы в дереве')
        print('0. Выйти')        
        print("")

    show_menu()
    
    menu = False
    while menu == False:
        command = input(f'{YELLOW}Введите действие:{RESET} ')
        if command == '0':
            print('Работа завершена')
            menu = True
        elif command == '9':
            if len(default_find_files + files_from_txt) == 0:
                print('Не указаны файлы для поиска')
                # show_menu()
            else:
                print_tree(default_start_directory, default_find_files + files_from_txt)
            
        elif command == '1':
            files_from_txt = pars_tapfiles_txt(default_txt)
            search_zips(default_start_directory, files_from_txt, default_output_directory)
            print('Поиск завершен')
        elif command == '2':
            if len(default_find_files) == 0:
                default_find_files = pars_console(input('Введите список файлов: '))
                search_zips(default_start_directory, default_find_files, default_output_directory)
            else:                                
                search_zips(default_start_directory, default_find_files, default_output_directory)
        elif command == '5':                                  
            default_find_files = pars_console(input('Введите список файлов: '))
            print('Список файлов для поиска изменён')

        elif command == '6':            
            default_start_directory = input('Укажите папку для поиска: ')
            print('Папка поиска изменена')

        elif command == '7':            
            default_output_directory = input('Укажите папку распаковки: ')
            print('Папка распаковки изменена')
            
        elif command == '3':
            show_menu()
        elif command == '4':
            show_settings()            
            
        else:
            print('Не корректная команда, попробуйте еще')

main()