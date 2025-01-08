"""
Необходимо создать класс Bank со следующими свойствами:
Атрибуты объекта:
balance - баланс банка (int)
lock - объект класса Lock для блокировки потоков.

Методы объекта:
Метод deposit:
Будет совершать 100 транзакций пополнения средств.
Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
Метод take:
Будет совершать 100 транзакций снятия.
Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
В начале должно выводится сообщение "Запрос на <случайное число>".
Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, 
уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" 
и заблокировать поток методом acquire.
Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.
После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".

По итогу вы получите скрипт разблокирующий поток до баланса равному 500 и больше или блокирующий, 
когда происходит попытка снятия при недостаточном балансе.
"""

import random
import threading
import time


class Bank:
    number_of_transactions = 100

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(self.number_of_transactions):
            self.add_random_amount_to_balance()
            self.unlock_if_met_conditions()
            time.sleep(0.01)

    def unlock_if_met_conditions(self):
        if self.balance >= 500 and self.lock.locked():
            self.lock.release()

    def add_random_amount_to_balance(self):
        amount = self.get_random_amount()
        self.balance += amount
        print(f'Пополнение: {amount}. Баланс: {self.balance}.')

    def get_random_amount(self):
        return random.randint(50, 500)

    def take(self):
        for _ in range(self.number_of_transactions):
            amount = self.get_random_amount()
            print(f'Запрос на снятие {amount}.')
            
            if amount <= self.balance:
                self.substract_random_amount_form_balance(amount)
            else:
                self.decline_and_lock()
            time.sleep(0.01)

    def substract_random_amount_form_balance(self, amount):
        self.balance -= amount
        print(f'Снятие: {amount}. Баланс: {self.balance}')

    def decline_and_lock(self):
        print('Запрос отклонён, недостаточно средств')
        self.lock.acquire()

def main():
    bank = Bank()

    # Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
    thread_1 = threading.Thread(target=Bank.deposit, args=(bank,))
    thread_2 = threading.Thread(target=Bank.take, args=(bank,))

    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

    print(f'Итоговый баланс: {bank.balance}')

if __name__ == '__main__':
    main()




    