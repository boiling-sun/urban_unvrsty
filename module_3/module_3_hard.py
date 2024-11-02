"""
Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99


Примечания (рекомендации):
Весь подсчёт должен выполняться одним вызовом функции.
Рекомендуется применить рекурсивный вызов функции, для каждой внутренней структуры.
Т.к. каждая структура может содержать в себе ещё несколько элементов, можно использовать параметр *args
Для определения типа данного используйте функцию isinstance.

Файл с кодом (module_3_hard.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий с файлом решения.

Успехов!

"""


def main():
    data_structure = [
        [1, 2, 3],
        {'a': 4, 'b': 5},
        (6, {'cube': 7, 'drum': 8}),
        "Hello",
        ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]
    result = calculate_structure_sum(data_structure)
    print(result) # 99

def calculate_structure_sum(*args):
    result = 0
    
    for arg in args:
        if isinstance(arg, (int, float)):
            result += arg
        elif isinstance(arg, str):
            result += len(arg)
        elif isinstance(arg, dict):
            result += calculate_structure_sum(*list(arg.items()))
        elif isinstance(arg, (list, tuple)):
            result += calculate_structure_sum(*arg)
        elif isinstance(arg, set):
            result += calculate_structure_sum(*list(arg))
    
    return result        
        
if __name__ == '__main__':
    main()