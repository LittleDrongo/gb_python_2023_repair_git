import os
import zipfile

start_directory = "C:/DELETE_ME"
find_files = [
    'нужный_файл', 'нужный_файл_2', 'нужный_файл_3',
    ]  # Список файлов для поиска
output_patch = "C:/DELETE_ME_2"

YELLOW = "\033[33m"
RESET = "\033[0m"

def print_tree(directory, indent="", level=0, find_files=None):
    if find_files is None:
        find_files = set()

    items = os.listdir(directory)
    items.sort()

    for item in items:
        item_path = os.path.join(directory, item)

        if os.path.isdir(item_path):
            print(f"{indent}├── 🖿  {item}")  # Папка
            print_tree(item_path, indent + "│   ", level + 1, find_files)
        elif zipfile.is_zipfile(item_path):
            print(f"{indent}├── 🗀  {item}")  # Архив
            with zipfile.ZipFile(item_path, 'r') as zipf:
                for zip_item in zipf.namelist():
                    if zip_item.endswith('/'):
                        print(f"{indent}│   └── 🗀 {zip_item}")  # Подпапка в архиве
                    else:
                        if any(find_file in zip_item for find_file in find_files):
                            print(f"{indent}│   └──── {YELLOW}{zip_item}{RESET}")  # Подсветка файла
                            zipf.extract(zip_item, os.path.join(output_patch))
                            # zipf.extract(zip_item, os.path.join(output_patch, zip_item))
                        else:
                            print(f"{indent}│   └──── {zip_item}")  # Файл в архиве
        else:
            if any(find_file in item for find_file in find_files):
                print(f"{indent}└──── {YELLOW}{item}{RESET}")  # Подсветка файла
            else:
                print(f"{indent}└──── {item}")  # Файл в папке


os.system('cls')  # Очистить консоль
print(start_directory)
print_tree(start_directory, find_files=find_files)