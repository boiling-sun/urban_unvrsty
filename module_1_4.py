
def main():
    num_of_tasks = 12
    spent_hours = 1.5
    course_name = 'Python'
    time_per_task = spent_hours / num_of_tasks
    print(f'Курс: {course_name},', f'всего задач: {num_of_tasks},', 
          f'затрачено часов: {spent_hours},', f'среднее время выполнения {time_per_task}.')
    

if __name__ == '__main__':
    main()