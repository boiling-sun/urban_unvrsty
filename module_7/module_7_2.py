"""
Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для 
записи, strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), 
а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
"""
import os

def custom_write(file_name, strings):
    """
    Записывает в файл file_name все строки из списка strings, каждая на новой строке.
    Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), 
    а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() 
    перед записью.
    """
    path = os.path.join('module_7', file_name)
    strings_positions = {}
    with open(path, 'w', encoding='utf-8') as f:
        for i, string in enumerate(strings, 1):
            strings_positions[i, f.tell()] = string
            f.write(string + '\n')
    return strings_positions

def main():
    info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

if __name__ == '__main__':
    main()
