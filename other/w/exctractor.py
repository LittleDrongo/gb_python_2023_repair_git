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
        for item in zip_file.infolist():
            if item.filename in target_files:
                extracted_file_name = item.filename
                output_file_path = os.path.join(output_path, extracted_file_name)

                while os.path.exists(output_file_path):
                    extracted_file_name = get_unique_filename(output_path, extracted_file_name)
                    print(f"Распакован файл: {extracted_file_name}")
                    output_file_path = os.path.join(output_path, extracted_file_name)

                with zip_file.open(item) as source, open(output_file_path, 'wb') as destination:
                    destination.write(source.read())

def search_zips(directory, target_files, output_path):                                     # Рекурсивный поиск архивов Zip и последующий вызов функции
    for root, dirs, zips in os.walk(directory):
        for file in zips:
            if file.endswith(".zip"):
                file_path = os.path.join(root, file)
                
                # print("Просмотрен ZIP:", file_path)
                extract_necessary_files(file_path, target_files, output_path)