"""
Даны несколько списков, состоящих из строк
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

В переменную first_result запишите список созданный при помощи сборки 
состоящий из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.

В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) 
одинаковой длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)

В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение 
будет строка-длина строки. Значения строк будут перебираться из объединённых вместе списков first_strings и 
second_strings. Условие записи пары в словарь - чётная длина строки.
"""

def main():
    first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
    second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

    first_result = [len(s) for s in first_strings if len(s) >= 5]
    print(first_result) # [10, 8, 8]

    second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]
    print(second_result) # [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]

    third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}
    print(third_result) # {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}

if __name__ == '__main__':
    main()