"""
Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых будут обладать методами 
изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны интерфейсы 
взаимодействия (методы) - геттеры и сеттеры.

Подробное ТЗ:

Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, 
предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны 
целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, 
то не изменять, в противном случае - менять.

Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)

Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, 
то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]

Примечания (рекомендации):
Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!
"""

class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=False):
        #self.__sides = self.set_sides(sides)
        #self.__color = self.set_color(color)
        self.color = color
        self.sides = sides
        self.filled = filled

    #def get_color(self):
    @property
    def color(self):
        """Получает цвет фигуры."""
        return self.__color
    
    def __is_valid_color(self, rgb):
        """
        Проверяет корректность переданных значений перед установкой нового цвета:
        r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
        """
        return all(isinstance(i, int) and i in range(0, 256) for i in rgb)
    
    @color.setter
    def color(self, rgb):
        """
        Устанавливает цвет объекта в формате RGB.

        При попытке установить цвет проверяется, был ли уже инициализирован,  __color.
        Если атрибут не инициализирован и переданный цвет невалиден, цвет устанавливается 
        на (0, 0, 0). Если атрибут уже существует, а новый цвет валиден, 
        цвет успешно изменяется и выводится сообщение об изменении цвета. 

        Если новый цвет невалиден, выводится сообщение об ошибке, и цвет не изменяется.

        Параметры:
        rgb (iterable): Новый цвет в формате RGB, представленный в виде 
        последовательности из трех чисел (например, список или кортеж), 
        где каждое число должно находиться в диапазоне от 0 до 255.
        """
        try: 
            self.__color
        except AttributeError:
            if not self.__is_valid_color(rgb):
                rgb = [0, 0, 0]
        else:
            if self.__is_valid_color(rgb):
                print(f'Цвет успешно изменен: {rgb}')
            else:
                print(f'Некорректный формат цвета {rgb}')
                rgb = None
        finally:
            if rgb:
                self.__color = list(rgb)

    #def get_sides(self):
    @property
    def sides(self):
        """Получает размер сторон фигуры."""
        return self.__sides
    
    def __is_valid_sides(self, new_sides):
        """
        Принимает неограниченное кол-во сторон, возвращает True если все стороны - 
        целые положительные числа и кол-во новых сторон совпадает с текущим, 
        False - во всех остальных случаях.
        """
        if not new_sides:
            return False
        elif isinstance(new_sides, int):
            return new_sides > 0 
        else:
            return (len(new_sides) == self.sides_count and 
                all(isinstance(side, int) and side > 0 for side in new_sides))

    #def set_sides(self, *new_sides):
    @sides.setter
    def sides(self, new_sides):
        """
        Устанавливает размеры сторон фигуры.

        Если при создании объекта количество переданных сторон не соответствует
        заданному sides_count, то создается массив с единичными сторонами в 
        количестве, необходимом для фигуры. При попытке изменить размеры 
        существующей фигуры проверяется, действительны ли новые размеры. 

        Если размеры валидны, они устанавливаются как новые стороны фигуры. 
        В противном случае, если размеры невалидны и атрибут __sides 
        еще не был инициализирован, создается массив с единичными сторонами 
        в количестве sides_count. Если же атрибут __sides уже существует, 
        выводится сообщение о том, что размеры неверные и фигура остается 
        без изменений.

        Параметры:
        new_sides (iterable): Новые размеры сторон фигуры. Должны быть числовыми 
        значениями и соответствовать условиям валидации, определенным в методе 
        __is_valid_sides().
        """
        try: 
            self.__sides
        except AttributeError:
            if not self.__is_valid_sides(new_sides):
                new_sides = [1] * self.sides_count
        else:
            if self.__is_valid_sides(new_sides):
                print(f'Размер фигуры успешно изменен на {new_sides}')
            else:
                print(f'Переданы неверные размеры. Размер фигуры не изменился.')
                new_sides = None
        finally:
            if new_sides:
                if isinstance(new_sides, int):
                    new_sides = (new_sides,)
                self.__sides = list(new_sides)    

    def __len__(self):
        """Возвращает сумму сторон (периметр) фигуры."""
        if len(self.sides) == 1:
            return self.sides[0]
        else:
            return sum(self.sides)
    
    def __str__(self):
        return f'Фигура {self.__class__.__name__} с цветом {self.color} и сторонами {self.sides}' + \
            f' {"заполнена" if self.filled else "не заполнена"}'
    
    def fill(self):
        """Меняет атрибут filled на противоположный."""
        self.filled = not self.filled


class Circle(Figure): 
    sides_count = 1

    def __init__(self, color, *sides):   
        super().__init__(color, *sides)
        #self.__radius = self.get_radius()

    #def get_radius(self):
    @property
    def radius(self):
        """Получает радиус Circle."""
        return self.sides[0] / (2 * 3.14)
        
    #def get_square(self):
    @property
    def square(self):
        """Получает площадь Circle."""
        #return 3.14 * self.get_radius() ** 2
        return 3.14 * self.radius ** 2
    
    
class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    #def set_sides(self, new_side):
    @Figure.sides.setter
    def sides(self, new_sides):
        """
        Дополняет сеттер родительского класса для класса Triangle. 
        Принимает такие new_sides, которые составят валидный треугольник.   
        """
        if len(new_sides) == self.sides_count: 
            # проверка на валидность длин строн  
            a, b, c = new_sides
            if a + b <= c or a + c <= b or b + c <= a:
                new_sides = None
        super(Triangle, Triangle).sides.fset(self, new_sides)

    #def get_square(self):
    @property
    def square(self):
        """Получает площадь Triangle по формуле Герона."""
        a, b, c = self.sides
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area    
    

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    #def set_sides(self, new_side):
    @Figure.sides.setter
    def sides(self, new_sides):
        """
        Дополняет сеттер родительского класса для класса Cube. 
        Ожидает единичное значение параметра new_sides для создания куба, либо 
        sides_count одинаковых целочисленных значений  
        """
        if isinstance(new_sides, int):
            new_sides = (new_sides,) * self.sides_count
        elif len(new_sides) == 1:
            new_sides = new_sides * self.sides_count
        elif len(new_sides) == self.sides_count: 
            if len(set(new_sides)) != 1:
                new_sides = None
        super(Cube, Cube).sides.fset(self, new_sides)

    #def get_square(self):
    @property
    def square(self):
        """Получает площадь Cube."""
        return 6 * self.sides[0] ** 2

    #def get_volume(self):
    @property
    def volume(self):
        """Получает объем Cube."""
        return self.sides[0] ** 3
    

def main():

    print('Создание фигур: с корректными параметрами')
    circle = Circle((200, 200, 100), 10) 
    print(circle)
    cube = Cube((222, 35, 130), 8)
    print(cube)
    triangle = Triangle((255, 67, 255), 3, 4, 5)
    print(triangle, end='\n\n')

    print('Создание фигур: с некорректными параметрами')
    incorrect_circle = Circle((200, 350, 100), 10, 4, 2) 
    print(incorrect_circle)
    incorrect_cube = Cube((272, 35, 130), 6, 5, 4, 3, 2, 1)
    print(incorrect_cube)
    incorrect_cube = Cube((255, 35, 130), 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7)
    print(incorrect_cube)
    incorrect_triangle = Triangle((-9, 255, 255), 1, 2, 3)
    print(incorrect_triangle, end='\n\n')

    print('Проверка на изменение цветов: c корректным цветом')
    print(circle)
    #circle.set_color(55, 66, 77) # Изменится
    circle.color = (55, 66, 77) # Изменится
    #print(circle1.get_color())
    print(circle, '\n')
    print('Проверка на изменение цветов: c некорректным цветом')
    print(cube)
    #cube.set_color(300, 70, 15) # Не изменится
    cube.color = (300, 70, 15) # Не изменится
    #print(cube1.get_color())
    print(cube, '\n')

    print('Проверка на изменение сторон: c корректными параметрами')
    print(circle)
    #circle.set_sides(15) # Изменится
    circle.sides = 15 # Размер фигуры успешно изменен на 15
    #print(circle1.get_sides())
    print(circle)
    print(cube)
    #cube.set_sides(5) # Изменится
    cube.sides = 5 # Размер фигуры успешно изменен на (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    print(cube)
    cube.sides = 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6 # Размер фигуры успешно изменен на (6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6)
    print(cube)
    print(triangle)
    triangle.sides = 7, 10, 11 # Размер фигуры успешно изменен на (7, 10, 11)
    print(triangle, '\n')

    print('Проверка на изменение сторон: c некорректными параметрами')
    print(circle)
    circle.sides = 0 # Переданы неверные размеры. Размер фигуры не изменился.
    #print(circle1.get_sides())
    print(circle)
    print(cube)
    #cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    cube.sides = 5, 3, 12, 4, 5 # Переданы неверные размеры. Размер фигуры не изменился.
    #print(cube1.get_sides())
    print(cube)
    print(triangle)
    triangle.sides = 0.5, 2, 3 # Переданы неверные размеры. Размер фигуры не изменился.
    print(triangle, '\n')

    print('Проверка измерение длины фигуры:')
    print('Длина круга:', len(circle))
    print('Длина куба:', len(cube))
    print('Длина треугольника:', len(triangle), end='\n\n')

    print('Проверка измерение площади фигуры:')
    print(f'Площадь круга: {circle.square}')
    print(f'Площадь куба: {cube.square}')
    print(f'Площадь треугольника: {triangle.square}', end='\n\n')

    print('Проверка заполнения фигуры:')
    print(triangle)
    triangle.fill()
    print(triangle)
    triangle.fill()
    print(triangle, '\n')

    #print(cube1.get_volume())
    print(f'Проверка объёма куба: {cube.volume}')
    print(f'Проверка радиуса круга: {circle.radius}')


if __name__ == "__main__":
    main()
    
