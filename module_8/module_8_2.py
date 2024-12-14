"""
Напишите 2 функции:
Функция personal_sum(numbers):
Должна принимать коллекцию numbers.
Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError, 
увеличив счётчик incorrect_data на 1.
В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во 
некорректных данных.
Функция calculate_average(numbers)
Среднее арифметическое - сумма всех данных делённая на их количество.
Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и 
верните 0.
Также в numbers может быть записана не коллекция, а другие типы данных, например числа. Обработайте исключение 
TypeError выводя строку 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None.
"""

def personal_sum(numbers):
    """
    Функция для подсчёта суммы чисел в коллекции numbers.
    При встрече некорректных типов данных увеличивает счётчик incorrect_data.
    Возвращает кортеж: (result, incorrect_data).
    """
    result, incorrect_data = 0, 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    """
    Функция для вычисления среднему арифметического из коллекции numbers.
    Использует personal_sum для подсчёта суммы. 
    Обрабатывает исключения: 
    - ZeroDivisionError: возвращает 0 для пустой коллекции.
    - TypeError: выводит сообщение о некорректном типе данных и возвращает None.
    """
    try:
        _ = iter(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    
    result, incorrect_data = personal_sum(numbers)
    try:
        return result / (len(numbers) - incorrect_data)
    except ZeroDivisionError:
        return 0

def main():
    print(f'Результат 1: {calculate_average("1, 2, 3")}') # Результат 1: 0
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Результат 2: 2.0
    print(f'Результат 3: {calculate_average(567)}') # Результат 3: None
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Результат 4: 26.5

if __name__ == '__main__':
    main()