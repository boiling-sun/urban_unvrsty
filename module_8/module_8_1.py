"""
Реализуйте следующую функцию:
add_everything_up, будет складывать числа(int, float) и строки(str)

Описание функции:
add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
TypeError - когда a и b окажутся разными типами (числом и строкой), 
то возвращать строковое представление этих двух данных вместе (в том же порядке). 
Во всех остальных случаях выполнять стандартные действия.
"""

def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        result = f'{a}{b}'
    else: 
        result = f'{result:.2f}'
    finally:
        return result

def main():
    print(add_everything_up(123.456, 'строка'))  # 123.456строка
    print(add_everything_up('яблоко', 4215))  # яблоко4215
    print(add_everything_up(123.456, 7))  # 130.46

if __name__ == '__main__':
    main()