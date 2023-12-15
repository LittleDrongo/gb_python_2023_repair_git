from get_filelist_from_email import *
import time
import subprocess

interval_seconds = 10 #Проверять почту каждые 10 секунд.

while True:
    try:        
        get_list_to_search()            # Выполняем команду       
        time.sleep(interval_seconds)    # Ждем указанный интервал
    
    except subprocess.CalledProcessError as e:
        print(f"Ошибка работы цикла")