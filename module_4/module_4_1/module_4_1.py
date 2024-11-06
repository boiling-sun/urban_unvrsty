"""
Создайте модули fake_math и true_math в которых создайте функции отвечающие за деление, но разными способами.

Пункты задачи:
Создайте модули fake_math и true_math.
Напишите функции divide в обоих методах. Разница между этими функциями - возвращаемое значение.
Создайте модуль module_4_1 (если ещё не создан), импортируйте в него функции divide из модулей fake_math и true_math, назвав их разными именами на своё усмотрение, чтобы не было конфликтов имён, при помощи оператора as.
Запустите эти функции в модуле module_4_1, передав первым аргументом произвольное число отличное от 0, вторым аргументом - 0
Выведи результаты вызовов этих функций на экран(в консоль).
"""

from fake_math import divide as fake_divide
from true_math import divide as true_divide

def main():
    result1 = fake_divide(69, 3)
    result2 = fake_divide(3, 0)
    result3 = true_divide(49, 7)
    result4 = true_divide(15, 0)
    print(result1) # 23.0
    print(result2) # Ошибка
    print(result3) # 7.0
    print(result4) # inf

if __name__ == '__main__':
    main()
