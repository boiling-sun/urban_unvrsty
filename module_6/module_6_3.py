"""
Необходимо написать 5 классов:

Animal - класс описывающий животных.
Класс обладает следующими атрибутами:
live = True
sound = None - звук (изначально отсутствует)
_DEGREE_OF_DANGER = 0 - степень опасности существа
Объект этого класса обладает следующими атрибутами:
_cords = [0, 0, 0] - координаты в пространстве.
speed = ... - скорость передвижения существа (определяется при создании объекта)
И методами:
move(self, dx, dy, dz), который должен менять соответствующие кооординаты в _cords на dx, dy и dz в том же порядке, 
где множетелем будет являтся speed. Если при попытке изменения координаты z в _cords значение будет меньше 0, 
то выводить сообщение "It's too deep, i can't dive :(" , 
при этом изменения не вносяться.
get_cords(self), который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful, i'm attacking you 0_0" , если равно или больше.
speak(self), который выводит строку со звуком sound.

Bird - класс описывающий птиц. Наследуется от Animal.
Должен обладать атрибутом:
beak = True - наличие клюва
И методом:
lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"

AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
В этом классе атрибут _DEGREE_OF_DANGER = 3.
Должен обладать методом:
dive_in(self, dz) - где dz изменение координаты z в _cords. Этот метод должен всегда уменьшать координату z 
в _coords. Чтобы сделать dz положительным, берите его значение по модулю (функция abs). 
Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2)

PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.
В этом классе атрибут _DEGREE_OF_DANGER = 8.

Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal. 
Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
Объект этого класса должен обладать одним дополнительным атрибутом:
sound = "Click-click-click" - звук, который издаёт утконос
"""
from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._coords = [0, 0, 0]
        self.speed = speed
    
    def move(self, dx, dy, dz):
        """
        Меняет соответствующие кооординаты в _cords на dx, dy и dz в том же порядке, 
        где множетелем будет являтся speed. Если при попытке изменения координаты 
        z в _cords значение будет меньше 0, то выводить сообщение "It's too deep, i can't dive :(" , 
        при этом изменения не вносяться.
        """
        if self.speed == 0:
            return
        
        if (new_z := self._coords[2] + dz * self.speed) < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._coords[0] += dx * self.speed
            self._coords[1] += dy * self.speed
            self._coords[2] = new_z

    def get_coords(self): 
        print(f"X: {self._coords[0]} Y: {self._coords[1]} Z: {self._coords[2]}")
    
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed) 

    def lay_eggs(self):
        number_of_eggs = randint(1, 4)
        if number_of_eggs == 1:
            print(f"Here is {number_of_eggs} egg for you.")
        else:
            print(f"Here are {number_of_eggs} eggs for you")


class AquaticAnimal(Animal):
    """
    Должен обладать методом:
    """
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        """ 
        dz изменение координаты z в _cords. Этот метод должен всегда уменьшать координату z 
        в _coords. Чтобы сделать dz положительным, берите его значение по модулю (функция abs). 
        Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2) 
        """
        new_z = self._coords[2] - abs(dz) * self.speed // 2
        self._coords[2] = new_z


class PoisonousAnimal(Animal):
     _DEGREE_OF_DANGER = 8

     def __init__(self, speed):
         super().__init__(speed)


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)


def main():
    db = Duckbill(10)

    print(f'Жив ли утконос: {db.live}') # True
    print(f'Есть ли клюв у утконоса: {db.beak}') # True

    print('Утконос издает звуки: ', end='')
    db.speak() # Click-click-click
    print('Утконос атакует: ', end='')
    db.attack() # Be careful, i'm attacking you 0_0

    print('Утконос совершает маневр: ', end='')
    db.move(1, 2, 3) 
    db.get_coords() # X: 10 Y: 20 Z: 30
    print('Утконос ныряет: ', end='')
    db.dive_in(6) 
    db.get_coords() # X: 10 Y: 20 Z: 0

    print('Утконос откладывает яйца: ', end='')
    db.lay_eggs() # Here are 4 eggs for you

if __name__ == '__main__':
    main()




    

