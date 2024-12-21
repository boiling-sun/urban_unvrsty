"""
Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор, 
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
"""

import itertools

def all_variants(text):
    for i in range(len(text)):
        for j in itertools.combinations(text, i + 1):
            result = ''.join(j)
            if result in text:
                yield result

def main():
    a = all_variants("abc")
    for i in a:
        print(i)

if __name__ == '__main__':
    main()