"""
Необходимо дополнить класс House следующими специальными методами:
__eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать 
результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
__add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
__radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
Остальные методы арифметических операторов, где self - x, other - y:

Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики 
перед выполняемыми действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
isinstance(other, int) - other указывает на объект типа int.
isinstance(other, House) - other указывает на объект типа House.
"""

from module_5_2 import House_2


class House_3(House_2):

    @staticmethod
    def is_house(object):
        """ Возвращает True, если количество этажей одинаковое у self и у other."""
        return isinstance(object, House_2)
    
    def __eq__(self, other):
        """ Возвращает True, если количество этажей одинаковое у self и у other."""
        if House_3.is_house(other):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        """ Возвращает True, если количество этажей у self меньше, чем у other."""
        if House_3.is_house(other):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        """ Возвращает True, если количество этажей у self меньше либо равно other."""
        if House_3.is_house(other):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        """ Возвращает True, если количество этажей у self больше, чем у other."""
        if House_3.is_house(other):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        """ Возвращает True, если количество этажей у self больше либо равно other."""
        if House_3.is_house(other):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        """ Возвращает True, если количество этажей разное у self и у other."""
        if House_3.is_house(other):
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

def main():
    h1 = House_3('ЖК Эльбрус', 10)
    h2 = House_3('ЖК Акация', 20)

    print(h1) # Название: ЖК Эльбрус, кол-во этажей: 10
    print(h2) # Название: ЖК Акация, кол-во этажей: 20

    print(h1 == h2) # __eq__ False

    h1 = h1 + 10 # __add__
    print(h1) # Название: ЖК Эльбрус, кол-во этажей: 20
    print(h1 == h2) # True

    h1 += 10 # __iadd__
    print(h1) # Название: ЖК Эльбрус, кол-во этажей: 30

    h2 = 10 + h2 # __radd__
    print(h2) # Название: ЖК Акация, кол-во этажей: 30

    h2 = 10.0 + h2 # Операция не поддерживается.
    print(h2) # Название: ЖК Акация, кол-во этажей: 30

    print(h1 > h2) # __gt__ False
    print(h1 >= h2) # __ge__ True
    print(h1 < h2) # __lt__ False
    print(h1 <= h2) # __le__ True
    print(h1 != h2) # __ne__ False


if __name__ == '__main__':
    main()