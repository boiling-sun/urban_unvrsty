"""
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.

Комментарии к заданию:

Ключевая идея – использование вложенного for

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = ?
    filetime = ?
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = ?
    parent_dir = ?
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')



Так как в разных операционных системах разная схема расположения папок, тестировать проще всего в папке проекта 
(directory = “.”)
"""
import os
import time

def main():
    directory = "."

    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            filetime = os.stat(filepath).st_mtime
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт', 
                  f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


if __name__ == '__main__':
    main()

