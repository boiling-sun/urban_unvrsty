"""
Создайте 3 класса (2 из которых будут исключениями):
Класс Car должен обладать следующими свойствами:
Атрибут объекта model - название автомобиля (строка).
Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. 
Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Атрибут __numbers - номера автомобиля (строка).
Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. 
Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.

Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - 
сообщение, которое будет выводиться при выбрасывании исключения.

Работа методов __is_valid_vin и __is_valid_numbers:
__is_valid_vin
Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', 
если передано не целое число. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', 
если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
Возвращает True, если исключения не были выброшены.
__is_valid_numbers
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', 
если передана не строка. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', 
переданная строка должна состоять ровно из 6 символов.
Возвращает True, если исключения не были выброшены.

ВАЖНО!
Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта 
(в __init__ при объявлении атрибутов __vin и __numbers).
"""

class Car:
    """
    Класс Car представляет автомобиль с определённой моделью, VIN-номером и номерами.

    Атрибуты:
        model (str): Название автомобиля.
        __vin (int): VIN-номер автомобиля. Доступен только внутри класса.
        __numbers (str): Номера автомобиля. Доступен только внутри класса.

    Методы:
        __is_valid_vin(vin_number): Проверяет корректность VIN-номера.
        __is_valid_numbers(numbers): Проверяет корректность номеров автомобиля.
    """
    def __init__(self, model, vin, numbers):
        self.model = model
        self.vin = vin
        self.numbers = numbers

    @property
    def vin(self):
        return self.__vin

    @vin.setter
    def vin(self, the_vin):
        if self.__is_valid_vin(the_vin):
            self.__vin = the_vin

    def __is_valid_vin(self, vin_number):
        """
        Проверяет vin номер:
        - Выбрасывает IncorrectVinNumber с сообщением 
          'Некорректный тип vin номер', если не целое число.
        - Выбрасывает IncorrectVinNumber с сообщением 
          'Неверный диапазон для vin номера', если число вне диапазона 1000000-9999999.
        Возвращает True при отсутствии исключений.
        """
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип данных для vin номера')
        if vin_number not in range(1000000, 10000000):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True
        
    @property
    def numbers(self):
        return self.__numbers

    @numbers.setter
    def numbers(self, the_numbers):
        if self.__is_valid_numbers(the_numbers):
            self.__numbers = the_numbers

    def __is_valid_numbers(self, numbers):
        """
        Проверяет номера автомобилей:
        - Выбрасывает IncorrectCarNumbers с сообщением 
          'Некорректный тип данных для номеров', если не строка.
        - Выбрасывает IncorrectCarNumbers с сообщением 
          'Неверная длина номера', если строка не состоит из 6 символов.
        Возвращает True при отсутствии исключений.
        """
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номера')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


def main():
    try:
        first = Car('Model1', 1000000, 'f123dj')
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан') # Model1 успешно создан

    try:
        second = Car('Model2', 300, 'т001тр')
    except IncorrectVinNumber as exc:
        print(exc.message) # Неверный диапазон для vin номера
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Model3', 2020202, 'нет номера')
    except IncorrectVinNumber as exc:
        print(exc.message) 
    except IncorrectCarNumbers as exc:
        print(exc.message) # Неверная длина номера
    else:
        print(f'{third.model} успешно создан')

if __name__ == '__main__':
    main()