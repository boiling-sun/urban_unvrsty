"""
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.

Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Инкапсулированный атрибут __file_name = 'products.txt'.
Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает 
единую строку со всеми товарами из файла __file_name.
Метод add(self, *products), который принимает неограниченное количество объектов класса Product. 
Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). 
Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
"""

class Product:
    """
    Атрибут name - название продукта (строка).
    Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
    Атрибут category - категория товара (строка).
    Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. 
    """
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
    

class Shop:
    def __init__(self):
        self.__file_name = 'module_7/products.txt'

    def get_products(self):
        """
        Cчитывает всю информацию из файла __file_name, закрывает его и возвращает 
        единую строку со всеми товарами из файла __file_name.
        """
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            return file.read()
        
    def add(self, *products):
        """
        Метод add(self, *products), который принимает неограниченное количество объектов класса Product. 
        Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). 
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
        """
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if isinstance(product, Product):
                    if product.name in self.get_products():
                        print(f'Продукт {product.name} уже есть в магазине')
                    else:
                        file.write(f'{product}\n')

def main():
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Tomato', 5.5, 'Vegetables')

    print(p2) # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())

if __name__ == '__main__':
    main()