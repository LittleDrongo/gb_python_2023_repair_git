from get_filelist_from_email import *
import time
import subprocess

password_menu = input('Введите пароль: ')
smtp_params['smtp_password'] = password_menu
imap_params['imap_password'] = password_menu

default_start_directory = 'C:/Test/start_dr'
default_output_directory = 'C:/Test/outpute_dir'
auth_subj = 'CLR_001'

interval_seconds = 10 #Проверять почту каждые 10 секунд.

while True:
    try:        
        get_list_to_search()            # Выполняем команду       
        time.sleep(interval_seconds)    # Ждем указанный интервал
    
    except subprocess.CalledProcessError as e:
        print(f"Ошибка работы цикла")