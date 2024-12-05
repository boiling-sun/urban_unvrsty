"""
Напишите код, который форматирует строки для следующих сценариев.
Укажите переменные, которые должны быть вставлены в каждую строку:

Комментарии к заданию:
В русском языке окончания слов меняются (1 участник, 2 участника), пока что давайте не обращать на это внимания.
Переменные challenge_result, tasks_total, time_avg можно задать вручную или рассчитать. Например, для challenge_result:
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
result = ‘Победа команды Мастера кода!’
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
result = ‘Победа команды Волшебники Данных!’
else:
result = ‘Ничья!’

Пример входных данных
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
"""

def challenge_result(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        return 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        return 'Победа команды Волшебники Данных!'
    else:
        return 'Ничья!'
    



def main():
    team1_num = 5  # количество участников первой команды
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    tasks_total = sum((score_1, score_2))
    time_avg = round((team1_time + team2_time) / tasks_total, 1)
    #challenge_result = 'Победа команды Волшебники данных!'

    # Использование %:
    print('В команде Мастера кода участников: %d!' % team1_num)
    print('Итого сегодня в командах участников: %d и %d!' % (team1_num, team2_num))

    #  Использование format():
    print('Команда Волшебники данных решила задач: {}!'.format(score_2))
    print('Волшебники данных решили задачи за {:.1f} с.!'.format(team1_time))

    #  Использование f-строк:
    print(f'Команды решили {score_1} и {score_2} задач.')
    print(f'Результат битвы: {challenge_result(score_1, score_2, team1_time, team2_time)}')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

if __name__ == '__main__':
    main()

