"""
Задача "Распаковка":
1.Функция с параметрами по умолчанию:
Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
Функция должна выводить эти параметры.
Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
2.Распаковка параметров:
Создайте список values_list с тремя элементами разных типов.
Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
3.Распаковка + отдельные параметры:
Создайте список values_list_2 с двумя элементами разных типов
Проверьте, работает ли print_params(*values_list_2, 42)
"""


def print_params(a=1, b='строка', c=True):
    print(a, b, c)

def main():
    # 1.Функция с параметрами по умолчанию:
    print_params() # 1 строка True
    print_params(2, 'char', None) # 2 text None
    print_params(3, []) # 3 [] True
    print_params(b=25) # 1 25 True
    print_params(c=[1,2,3]) #1 строка [1, 2, 3]
    # 2.Распаковка параметров:
    values_list = [2, 'string', False]
    print_params(*values_list) # 2 string False
    values_dict = {'a': 2.2, 'b': (0, 1), 'c': {}}
    print_params(**values_dict) # 2.2 (0, 1) {}
    # 3.Распаковка + отдельные параметры:
    values_list_2 = [{}, 'The Answer to the Ultimate Question of Life, The Universe, and Everything is']
    print_params(*values_list_2, 42)


if __name__ == '__main__':
    main()
