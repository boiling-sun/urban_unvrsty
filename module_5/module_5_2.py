"""
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".

Необходимо дополнить класс House следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

"""

from module_5_1 import House_1


class House_2(House_1):
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    
def main():
    h1 = House_2('ЖК Эльбрус', 10)
    h2 = House_2('ЖК Акация', 20)

    # __str__
    print(h1) # Название: ЖК Эльбрус, кол-во этажей: 10
    print(h2) # Название: ЖК Акация, кол-во этажей: 20

    # __len__
    print(len(h1)) # 10
    print(len(h2)) # 20

if __name__ == '__main__': 
    main()