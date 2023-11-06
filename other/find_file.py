import os
import zipfile

output_folder = 'C:/DELETE_ME_2'  # Укажите папку, куда извлечь файлы
root_folder = 'C:/DELETE_ME'
find_files = ['нужный_файл', 'img_1.bmp', 'Yes!.bmp',]

# # ============ ИЩЕМ В ПАПКАХ

def fn_find_files_in_folder(root_folder, find_files):
    array_dir_files = []
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file in find_files:
                array_dir_files.append(os.path.join(root, file))

    return array_dir_files

# # ============ ИЩЕМ В АРХИВАХ

def fn_find_files_in_zip(root_folder, find_files):
    array_arc_files = []

    def search_in_zip(zip_path, find_file):
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            for zip_info in zip_file.infolist():
                if find_file in zip_info.filename:
                    array_arc_files.append(f"{zip_path}\\{zip_info.filename}")
                if zip_info.is_dir():
                    continue
                if zip_info.filename.endswith('/'):
                    continue
                if not zip_info.filename.startswith('__MACOSX/'):
                    with zip_file.open(zip_info) as zf:
                        with zf, open(os.devnull, 'wb') as f:
                            pass

    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.zip'):
                zip_path = os.path.join(root, file)
                for find_file in find_files:
                    search_in_zip(zip_path, find_file)

    return array_arc_files

# # ============ ВЫЗЫВАЕМ ФУНКЦИИ ========

found_dir_files = fn_find_files_in_folder(root_folder, find_files)
found_arc_files = fn_find_files_in_zip(root_folder, find_files)

# # ============ ВЫВОДИМ РЕЗУЛЬТАТ ========

for s in found_dir_files:
    print(s)

for s in found_arc_files:
    print(s)
