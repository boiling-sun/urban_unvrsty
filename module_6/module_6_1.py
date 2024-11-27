"""
Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), 
name - индивидуальное название каждого животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.

У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
В данном случае можно использовать принцип наследования, чтобы не дублировать код.

Метод eat должен работать следующим образом:
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.

Пункты задачи:
Создайте классы Animal и Plant с соответствующими атрибутами и методами
Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами. 
При необходимости переопределите значения атрибутов.
Создайте объекты этих классов.
"""


class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        """
        Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
        Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
        Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

        """
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f'{food} - не еда')        

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

class Fruit(Plant):
    edible = True
    def __init__(self, name):
        super().__init__(name)

def main():
    a1 = Predator('Тигр')
    a2 = Mammal('Обезьяна')
    p1 = Flower('Магнолия')
    p2 = Fruit('Ананас')

    print(f'Объект класса "Хищник": {a1.name}') 
    print(f'Объект класса "Млекопитающее": {a2.name}') 
    print(f'Объект класса "Цветок": {p1.name}') 
    print(f'Объект класса "Фрукт": {p2.name}\n') 

    print(f'Жив ли {a1.name}: {a1.alive}') # True
    print(f'Накормлен ли {a1.name}: {a1.fed}') # False
    print(f'Жив ли {a2.name}: {a2.alive}') # True
    print(f'Накормлен ли {a2.name}: {a2.fed}\n') # False

    print(f'Является ли {p1.name} съедобным: {p1.edible}') # False
    print(f'Является ли {p2.name} съедобным: {p2.edible}\n') # True

    print('Применение метода "eat": ')
    a1.eat(p1) # Хищник не стал есть Цветок
    a2.eat(p2) # Млекопитающее съело Фрукт
    
    print(f'Жив ли {a1.name}: {a1.alive}') # True
    print(f'Накормлен ли {a1.name}: {a1.fed}') # False
    print(f'Жив ли {a2.name}: {a2.alive}') # True
    print(f'Накормлен ли {a2.name}: {a2.fed}\n') # False

if __name__ == '__main__':
    main()
