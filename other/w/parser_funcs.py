def pars_tapfiles_txt(txt): #Парсит текстовый файл, возвращая массив строк с наименование файлов для поиска
    data = open(txt, 'r')
    arr_txt = []
    for line in data:
        arr_txt.append(line.rstrip())
    data.close
    return arr_txt

def pars_console(str):
    result = str.split()
    return result