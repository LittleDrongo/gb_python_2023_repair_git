import zipfile
import os

arhive = "C:/DELETE_ME/Папка/Архив_3.zip"  # Путь к ZIP-архиву
files = ['нужный_файл.txt', 'нужный_файл_2.txt', 'Yes!.bmp']
folder = "C:/DELETE_ME_2"  # Папка, в которую будут извлечены требуемые файлы

def extract_necessary_files(zip_file_path, target_files, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    def get_unique_filename(output_path, filename):
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
                    output_file_path = os.path.join(output_path, extracted_file_name)

                with zip_file.open(item) as source, open(output_file_path, 'wb') as destination:
                    destination.write(source.read())

extract_necessary_files(arhive, files, folder)