"""
Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
Атрибут name - имя рыцаря. (str)
Атрибут power - сила рыцаря. (int)

А также метод run, в котором рыцарь будет сражаться с врагами:
При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
В процессе сражения количество врагов уменьшается на power текущего рыцаря.
По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.

Пункты задачи:
Создайте класс Knight с соответствующими описанию свойствами.
Создайте и запустите 2 потока на основе класса Knight.
Выведите на экран строку об окончании битв.

Алгоритм выполнения кода:
# Создание класса
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
"""

from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        battle_days = self.fight_for_glory()
        print(f'{self.name} одержал победу спустя {battle_days} дней(дня)!')

    def fight_for_glory(self):
        battle_days = 0
        while self.enemies > 0:
            battle_days += 1
            self.enemies -= self.power
            sleep(1)
            print(f'{self.name} сражается {battle_days} день(дня)..., осталось {self.enemies} воинов.')
        return battle_days


def main():
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight('Sir Galahad', 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print('Все битвы закончились!')

if __name__ == '__main__':
    main()