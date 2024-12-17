"""
Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
int_list - список из чисел (int, float)
*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
Эта функция должна:
Вызвать каждую функцию к переданному списку int_list
Возвращать словарь, где ключом будет название вызванной функции, а значением - 
её результат работы со списком int_list.
Пункты задачи:
В функции apply_all_func создайте пустой словарь results.
Переберите все функции из *functions.
При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
Верните словарь results.
Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.
Пример результата выполнения программы:
"""

def apply_all_func(int_list, *functions):
    filtered_numbers = filter(lambda x: isinstance(x, (int, float)), int_list)
    int_list = list(filtered_numbers)
    filtered_funcs = filter(lambda x: callable(x), functions)
    functions = list(filtered_funcs)
    #return {func.__name__: func(int_list) for func in functions}
    result = {}
    for func in functions:
        try:
            result[func.__name__] = func(int_list)
        except Exception as e:
            result[func.__name__] = (e.__class__.__name__, *e.args)
    return result

def main():
    print(apply_all_func([6, 20, 15, 9], max, min)) #  {'max': 20, 'min': 6}
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted)) # {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
    print(apply_all_func([6, 20, '42', 15, 9], len, isinstance, {'foo': 1})) # {'len': 4, 'isinstance': ('TypeError', 'isinstance expected 2 arguments, got 1')}
if __name__ == '__main__':
    main()