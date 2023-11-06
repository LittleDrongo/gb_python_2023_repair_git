
import os
import zipfile

#01 Откройте ZIP-файл, где файл может быть путем к файлу (строкой), объектом, похожим на файл, или объектом, похожим на путь .
    # Параметр режима должен быть предназначен 'r'для чтения существующего файла, 'w'усечения и записи нового файла, 'a'добавления к существующему файлу или 'x'исключительного создания и записи нового файла. Если режим равен 'x'и файл ссылается на существующий файл, FileExistsErrorбудет создано. Если режим указан 'a'и файл ссылается на существующий ZIP-файл, к нему добавляются дополнительные файлы. Если файл не ссылается на ZIP-файл, к файлу добавляется новый ZIP-архив. Это предназначено для добавления ZIP-архива в другой файл (например, python.exe). Если режим есть 'a'и файл вообще не существует, он создается. Если mode равен 'r'или 'a', файл должен быть доступен для поиска.

#02 ZipFile.extract(member, path=None, pwd=None)
    # Extract a member from the archive to the current working directory; member must be its full name or a ZipInfo object. Its file information is extracted as accurately as possible. path specifies a different directory to extract to. member can be a filename or a ZipInfo object. pwd is the password used for encrypted files as a bytes object.
    # Returns the normalized path created (a directory or new file).
    # Note If a member filename is an absolute path, a drive/UNC sharepoint and leading (back)slashes will be stripped, e.g.: ///foo/bar becomes foo/bar on Unix, and C:\foo\bar becomes foo\bar on Windows. And all ".." components in a member filename will be removed, e.g.: ../../foo../../ba..r becomes foo../ba..r. On Windows illegal characters (:, <, >, |, ", ?, and *) replaced by underscore (_).
    # Changed in version 3.6: Calling extract() on a closed ZipFile will raise a ValueError. Previously, a RuntimeError was raised.

#03 Для извлечения одного файла применяется метод extract(), в который в качестве обязательного параметра передается имя извлекаемого файла:
    # myzip.extract("hello.txt")

target_files = ['hello.txt.txt', 'df4dceeaa5fd4702.txt', 'Yes!.bmp']
target_patch = "C:/DELETE_ME"
output_patch = "C:/DELETE_ME_2"
zip_file_path = "C:/DELETE_ME/02-02-2023/arc3.zip"

# Открываем архив
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Получаем список файлов и директорий внутри архива
    zip_contents = zip_ref.namelist()
    print("X-1")
    print(zip_contents)

    # Перебираем элементы архива
    for item in zip_contents:
        print("X-2")
        # Проверяем, если имя элемента находится в списке файлов для извлечения
        if any(item in target_files for item in zip_contents):
            for item in zip_contents:
                # item_path = os.path.join(item)
                if not os.path.isdir(item):
                        print(f'Кажется найден {item}')                
                        zip_ref.extract(item, os.path.join(output_patch, item))
            
        # if item in target_files:
        #     print(f'Найден: {item}') 


# if any(find_file in zip_item for find_file in find_files):
#     # print(f"{indent}│   └──── {YELLOW}{zip_item}{RESET}")  # Подсветка файла