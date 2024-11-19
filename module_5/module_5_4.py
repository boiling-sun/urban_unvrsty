"""
В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.
"""

class House:
    houses_history = []

    def __new__(cls, *args):
        """ При создании нового объекта записывает имя объекта в houses_history."""
        if args[0] not in cls.houses_history:
            cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        """
        Если new_floor является int, больше 0 и меньше или равно количеству этажей объекта, 
        выводит в консоль значения от 1 до new_floor включительно.
        """
        if 1 <= new_floor <= self.number_of_floors and isinstance(new_floor, int):
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        """ Возвращает количество этажей."""
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    @staticmethod
    def is_house(object):
        """ Возвращает True, если количество этажей одинаковое у self и у other."""
        return isinstance(object, House)
    
    def __eq__(self, other):
        """ Возвращает True, если количество этажей одинаковое у self и у other."""
        if House.is_house(other):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        """ Возвращает True, если количество этажей у self меньше, чем у other."""
        if House.is_house(other):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        """ Возвращает True, если количество этажей у self меньше либо равно other."""
        if House.is_house(other):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        """ Возвращает True, если количество этажей у self больше, чем у other."""
        if House.is_house(other):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        """ Возвращает True, если количество этажей у self больше либо равно other."""
        if House.is_house(other):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        """ Возвращает True, если количество этажей разное у self и у other."""
        if House.is_house(other):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        """ Увеличивает кол-во этажей на переданное значение value, возвращает self."""  
        if isinstance(value, int):
            self.number_of_floors += value
        else:
            print("Операция не поддерживается.")
        return self 

    def __radd__(self, value):
        """ 
        Возвращает результат вызова __add__. 
        Эта функция вызывается только в том случае, если левый операнд 
        не поддерживает соответствующую операцию и операнды имеют разные типы.
        """
        return self.__add__(value)

    def __iadd__(self, value):
        """ 
        Возвращает результат вызова __add__. 
        изменение объекта на месте с использованием '+='
        """
        return self.__add__(value)    
    
    def __del__(self):
        """ Выводит строку при удалении объекта."""
        print(f'{self.name} снесён, но он останется в истории')

def main():
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history) # ['ЖК Эльбрус']
    h2 = House('ЖК Акация', 20)
    print(House.houses_history) # ['ЖК Эльбрус', 'ЖК Акация']
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history) # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

    # Удаление объектов
    del h2 # ЖК Акация снесён, но он останется в истории
    del h3 # ЖК Матрёшки снесён, но он останется в истории

    print(House.houses_history) # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

    # ЖК Эльбрус снесён, но он останется в истории


if __name__ == '__main__':
    main()