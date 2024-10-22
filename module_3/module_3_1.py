'''
Задача "Счётчик вызовов":
Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. 
К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
Давайте реализуем данную фишку самостоятельно!

Пункты задачи:
Создать переменную calls = 0 вне функций.
Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
Создать функцию string_info с параметром string и реализовать логику работы по описанию.
Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
Вывести значение переменной calls на экран(в консоль).
'''

CALLS = 0

def main():
    print(string_info('Capybara'))
    print(string_info('Armageddon'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
    print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
    print(CALLS)

def count_calls():
    """ Функция подсчитывающая вызовы остальных функций. """
    global CALLS
    CALLS += 1
    return

def string_info(string):
    """ 
    Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, 
    строку в верхнем регистре, строку в нижнем регистре. """
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    """ 
    Функция принимает два аргумента: строку и список, и возвращает True,   
    если строка находится в этом списке, False - если отсутствует. 
    Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
    """
    count_calls()
    return string.lower() in [s.lower() for s in list_to_search]

if __name__ == '__main__':
    main()
