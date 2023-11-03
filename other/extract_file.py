import os
import zipfile

output_folder = 'C:/DELETE_ME_2'  # Укажите папку, куда извлечь файлы
root_folder = 'C:/DELETE_ME'
find_files = ['img.bmp', 'img_1.bmp']


found_dir_files = []  # Здесь будут храниться полные пути к найденным файлам
found_arc_files = []  # Здесь будут храниться полные пути к найденным файлам в архивах

for root, dirs, files in os.walk(root_folder):
    for file in files:
        if file in find_files:
            found_dir_files.append(os.path.join(root, file))

# # ============ ИЩЕМ В АРХИВАХ

def find_files_in_zip(root_folder, find_files):
    found_arc_files = []

    def search_in_zip(zip_path, find_file):
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            for zip_info in zip_file.infolist():
                if find_file in zip_info.filename:
                    found_arc_files.append(f"{zip_path}\\{zip_info.filename}")
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

    return found_arc_files


# =================================


def find_and_extract_files(root_folder, output_folder, find_files):
    extracted_files = set()

    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.zip'):
                zip_file_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
                    for find_file in find_files:
                        if find_file in zip_file.namelist():
                            base_name, ext = os.path.splitext(find_file)
                            index = 1
                            while find_file in extracted_files:
                                index += 1
                                find_file = f"{base_name}_{index}{ext}"
                            
                            extracted_files.add(find_file)

                            extract_path = os.path.join(output_folder, find_file)
                            with zip_file.open(find_file) as source, open(extract_path, 'wb') as dest:
                                dest.write(source.read())
                            print(f'Extracted {find_file} from {zip_file_path} to {extract_path}')





found_arc_files = find_files_in_zip(root_folder, find_files)
find_and_extract_files(root_folder, output_folder, find_files)

for s in found_dir_files:
    print(s)

for s in found_arc_files:
    print(s)
