"""
Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.

Подготовка:
! Скачайте архив с файлами для считывания данных и распакуйте его в проект для дальнейшего использования. !
Выполнение:
Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
Создайте список названий файлов в соответствии с названиями файлов архива.
Вызовите функцию read_info для каждого файла по очереди (линейно) 
и измерьте время выполнения и выведите его в консоль.
Вызовите функцию read_info для каждого файла, используя многопроцессный подход: 
контекстный менеджер with и объект Pool. Для вызова функции используйте метод map, 
передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.
Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности, 
предварительно закомментировав другой.
"""

import os
import time

from multiprocessing import Pool


def read_info(file_name):
    """
    Создавать локальный список all_data.
    Открывать файл name для чтения.
    Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
    Во время считывания добавлять каждую строку в список all_data.
    """
    all_data = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            if not line:
                break
            else:
                all_data.append(line)
        
        # while True:
        #     line = f.readline()
        #     if not line:
        #         break
        #     else:
        #         all_data.append(line)

def format_filename(number):
    return os.path.join('.', 'Files', f'file {number}.txt') 

def workflow_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        time_delta = end_time - start_time
        print(f'{time_delta} секунд.')
    return wrapper

@workflow_time
def linear_execution(filenames):
    for filename in filenames:
        read_info(filename)

@workflow_time
def multiprocess_execution(filenames):
    with Pool() as p:
        p.map(read_info, filenames)

def main():
    filenames = [format_filename(number) for number in range(1, 5)]

    print('Линейный вызов: ', end='')
    linear_execution(filenames)

    print('Многопроцессный вызов: ', end='')
    multiprocess_execution(filenames)

if __name__ == '__main__':
    main()