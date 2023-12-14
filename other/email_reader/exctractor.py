import zipfile
import os

def extract_necessary_files(zip_file_path, target_files, output_path):

    
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    def get_unique_filename(output_path, filename):             # Уникальные названия файлов если в целевой папке есть файл с таким же названием
        base_name, ext = os.path.splitext(filename)
        counter = 1
        while True:
            new_filename = f"{base_name}_copy_{counter:02d}{ext}"
            full_path = os.path.join(output_path, new_filename)
            if not os.path.exists(full_path):
                return new_filename
            counter += 1

    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        found_files = []
        for item in zip_file.infolist():
            if item.filename in target_files:
                extracted_file_name = item.filename
                output_file_path = os.path.join(output_path, extracted_file_name)
                print(f"Найден файл: {output_file_path}")
                
                
                while os.path.exists(output_file_path):
                    temp = output_file_path
                    extracted_file_name = get_unique_filename(output_path, extracted_file_name)
                    print(f"{temp} переименован в: {extracted_file_name}")
                    output_file_path = os.path.join(output_path, extracted_file_name)


                with zip_file.open(item) as source, open(output_file_path, 'wb') as destination:
                    destination.write(source.read())
                    found_files.append(output_file_path)
                
    return found_files
    

def search_zips(directory, files, output):                                     # Рекурсивный поиск архивов Zip и последующий вызов функции
    unpacked_files_paths = []
    for root, dirs, zips in os.walk(directory):
        for file in zips:
            if file.endswith(".zip"):
                file_path = os.path.join(root, file)
                
                unpacked_files_paths.append(extract_necessary_files(file_path, files, output))
    return unpacked_files_paths