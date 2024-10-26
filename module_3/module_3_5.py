"""
Задача "Рекурсивное умножение цифр":
Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number 
и подсчитывает произведение цифр этого числа.

Примечания:
При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.

"""

def main():
    result_1 = get_multiplied_digits(40203)
    print(result_1) # 24
    result_2 = get_multiplied_digits(40203000)
    print(result_2) # 24
    result_3 = get_multiplied_digits(111111111111111) 
    print(result_3) # 1

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    
    if len(str_number) == 1:
        # возвращать 1, если first = 0, чтобы не обнулять значение
        if first:
            return first
        else:
            return 1
 
    return first * get_multiplied_digits(int(str_number[1:]))

if __name__ == '__main__':
    main()

