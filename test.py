"""
Задание "Средний балл":
Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":

На вход даны следующие данные:
Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
Например: 'Aaron' - [5, 3, 3, 5, 4]
Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

Вывод в консоль:
{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}


Примечания:
Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).
"""

GRADES = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
STUDENTS = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


def main():
    students = sorted(STUDENTS)
    average_grade = list(map(lambda grades: sum(grades) / len(grades), GRADES))
    #average_grade = [sum(grades) / len(grades) for grades in GRADES]
    gradebook = dict(zip(students, average_grade))
    print(gradebook)

if __name__ == '__main__':
    main()
