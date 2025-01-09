""" 
Необходимо имитировать ситуацию с посещением гостями кафе.
Создайте 3 класса: Table, Guest и Cafe.
Класс Table:
Объекты этого класса должны создаваться следующим способом - Table(1)
Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
Класс Guest:
Должен наследоваться от класса Thread (быть потоком).
Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
Обладать атрибутом name - имя гостя.
Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
Класс Cafe:
Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
Метод guest_arrival(self, *guests):
Должен принимать неограниченное кол-во гостей (объектов класса Guest).
Далее, если есть свободный стол, то сажать гостя за стол (назначать столу guest), запускать 
поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить 
сообщение "<имя гостя> в очереди".

Метод discuss_guests(self):
Этот метод имитирует процесс обслуживания гостей.
Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), 
то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и 
"Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
Далее запустить поток этого гостя (start)
Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
Table - стол, хранит информацию о находящемся за ним гостем (Guest).
Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).

Пример результата выполнения программы:
Выполняемый код:
class Table:
...
class Guest:
...
class Cafe:
...
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

Вывод на консоль (последовательность может меняться из-за случайного время пребывания гостя):
Maria сел(-а) за стол номер 1
Oleg сел(-а) за стол номер 2
Vakhtang сел(-а) за стол номер 3
Sergey сел(-а) за стол номер 4
Darya сел(-а) за стол номер 5
Arman в очереди
Vitoria в очереди
Nikita в очереди
Galina в очереди
Pavel в очереди
Ilya в очереди
Alexandra в очереди
Oleg покушал(-а) и ушёл(ушла)
Стол номер 2 свободен
Arman вышел(-ла) из очереди и сел(-а) за стол номер 2
.....
Alexandra покушал(-а) и ушёл(ушла)
Стол номер 4 свободен
Pavel покушал(-а) и ушёл(ушла)
Стол номер 3 свободен
Примечания:
Для проверки значения на None используйте оператор is (table.guest is None).
Для добавления в очередь используйте метод put, для взятия - get.
Для проверки пустоты очереди используйте метод empty.
Для проверки выполнения потока в текущий момент используйте метод is_alive.
"""
from queue import Queue
from random import randint
from threading import Thread
from time import sleep

class Table:
    """    
    Класс Table:
    Объекты этого класса должны создаваться следующим способом - Table(1)
    Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
    """
    def __init__(self, number):
        self.number = number
        self.guest = None

    def is_occupied(self):
        return False if self.guest is None else True
    
    @property 
    def guest(self):
        return self._guest
    
    @guest.setter
    def guest(self, guest_item):
        if guest_item is None or isinstance(guest_item, Guest):
            self._guest = guest_item
        else:
            raise ValueError(f'{guest_item} is not a Guest instance')
        
    def recieve_and_launch_guest(self, guest, flag=None):
        self.guest = guest
        self.guest.launch()
        if not flag:
            print(f'{guest.name} сел(-а) за стол номер {self.number}.')
        else:
            print(f'{self.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {self.number}')
    
    def guest_leaves(self):
        print(f'{self.guest.name} поел(-а) и ушёл(ушла)')
        self.guest = None      
        print(f'Стол номер {self.number} свободен')  

class Guest(Thread):
    """Класс Guest:
    Должен наследоваться от класса Thread (быть потоком).
    Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
    Обладать атрибутом name - имя гостя.
    Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        eating_time = self.get_random_eating_time()
        self.eat(eating_time)

    def get_random_eating_time(self):
        return randint(3, 10)
    
    def eat(self, seconds):
        sleep(seconds)
    
    def launch(self):
        self.start()

    def finished(self):
        return not self.is_alive()

class Cafe:
    """
    Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
    Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
    Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
    """
    def __init__(self, *tables) -> None:
        self.tables = tables
        self.queue = Queue()

    @property
    def tables(self):
        return self._tables
    
    @tables.setter
    def tables(self, table_items):
        self._tables = [table for table in table_items if isinstance(table, Table)]

    def guest_arrival(self, *guests):
        """    
        Должен принимать неограниченное кол-во гостей (объектов класса Guest).
        Далее, если есть свободный стол, то сажать гостя за стол (назначать столу guest), 
        запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
        Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue 
        и выводить сообщение "<имя гостя> в очереди".
        """
        for guest in guests:
            if vacant_table := self.find_vacant_table():
                vacant_table.recieve_and_launch_guest(guest)
            else:
                self.put_guest_in_queue(guest)

    def find_vacant_table(self):
        try:
            vacant_table = next(table for table in self.tables if not table.is_occupied())
            return vacant_table
        except StopIteration:
            return None
    
    def put_guest_in_queue(self, guest):
        self.queue.put(guest)
        print(f'{guest.name} в очереди.')

    def retrieve_guest_from_queue(self):
        return self.queue.get()

    def discuss_guests(self):
        """
        Метод discuss_guests(self):
        Этот метод имитирует процесс обслуживания гостей.
        Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
        Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), 
        то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и 
        "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
        Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), 
        то текущему столу присваивается гость взятый из очереди (queue.get()). 
        Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
        Далее запустить поток этого гостя (start)
        """
        while (occupied_tables := self.get_occupied_tables()):
            for table in occupied_tables:
                if table.guest.finished():
                    table.guest_leaves()
                    self.recieve_and_launch_next_guest(table)

    def get_occupied_tables(self):
        return [table for table in self.tables if table.is_occupied()]

    def recieve_and_launch_next_guest(self, table):
        if not self.queue.empty():
            next_guest = self.retrieve_guest_from_queue()
            table.recieve_and_launch_guest(next_guest, 1)
        
        
def main():
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()

if __name__ == '__main__':
    main()
