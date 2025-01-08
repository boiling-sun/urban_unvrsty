"""
Задача "Потоковая запись в файлы":
Необходимо создать функцию wite_words(word_count, file_name), где word_count - количество записываемых слов, 
file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с 
прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию wite_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
Запустите эти потоки методом start, не забыв сделать остановку основного потока при помощи join.
Также измерьте время затраченное на выполнение функций и потоков. 

Пример результата выполнения программы:
Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков

Вывод на консоль:
Завершилась запись в файл example1.txt
Завершилась запись в файл example2.txt
Завершилась запись в файл example3.txt
Завершилась запись в файл example4.txt
Работа потоков 0:00:34.003411 # Может быть другое время
Завершилась запись в файл example5.txt
Завершилась запись в файл example6.txt
Завершилась запись в файл example8.txt
Завершилась запись в файл example7.txt
Работа потоков 0:00:20.071575 # Может быть другое время

Записанные данные в файл должны выглядеть так:

Cледует заметить, что запись в example8.txt завершилась раньше, чем в example7.txt, 
т.к. потоки работали почти одновременно.
"""
import time
import os

from threading import Thread

def write_words(word_count, file_name):
    """
    Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с 
    прерыванием после записи каждого на 0.1 секунду.
    В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
    """
    formatted_file_name = os.path.join('module_10', file_name)
    with open(formatted_file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

def workflow_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        time_delta = end_time - start_time
        print(f'Время работы потоков: {time_delta} секунд.')
    return wrapper

@workflow_time
def main_thread_write_words(args):
    for word_count, file_name in args:
        write_words(word_count, file_name)

@workflow_time
def four_threads_write_words(args):
    threads = [Thread(target=write_words, args=(*arg, )) for arg in args]
    start_threads(threads)
    join_threads(threads)
        
def start_threads(threads):
    for thread in threads:
        thread.start()

def join_threads(threads):
    for thread in threads:
        thread.join()

def main():
    args_1 = [(word_count, f'example{i}.txt') for i, word_count in enumerate((10, 30, 200, 100), 1)]
    args_2 = [(word_count, f'example{i}.txt') for i, word_count in enumerate((10, 30, 200, 100), 5)]

    print(args_1, args_2)

    main_thread_write_words(args_1)
    four_threads_write_words(args_2)

if __name__ == '__main__':
    main()