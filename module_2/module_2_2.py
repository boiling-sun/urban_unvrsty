"""
Задача "Все ли равны?":
На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

Пункты задачи:
Если все числа равны между собой, то вывести 3
Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
Если равных чисел среди 3-х вообще нет, то вывести 0

"""

def main():
    first = int(input('Enter first number: ').strip())
    second = int(input('Enter second number: ').strip())
    third = int(input('Enter third number: ').strip())
    amount_of_numbers = len(set((first, second, third)))

    if amount_of_numbers == 1:
        print(3)
    elif amount_of_numbers == 2:
        print(2)
    else:
        print(0)

#    match amount_of_numbers:
#        case 1:
#            print(3)
#        case 2:
#            print(2)
#        case _:
#            print(0)
    

if __name__ == "__main__":
    main()