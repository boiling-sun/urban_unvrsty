"""
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции 
будет простым числом и "Составное" в противном случае.
"""

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result != 0:
            for i in range(3, abs(result)):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

def main():
    result = sum_three(2, 3, 6)
    print(result)
    result = sum_three(12, -12, 0)
    print(result)

if __name__ == '__main__':
    main()
