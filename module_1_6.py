def main():
    # - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
    my_dict = dict((('foo', 100), ('bar', 200), ('baz', 300)))
    # - Выведите на экран словарь
    print(f'Dictionary: {my_dict}')
    # - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
    print(f'Existing value: {my_dict['foo']}')
    print(f'Not existing value: {my_dict.get('spam')}')
    # - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
    my_dict.update([('eggs', 400), ('spam', 4000)])
    # - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
    print(f'Deleted value: {my_dict.pop('foo')}')
    print(f'Modified dictionary: {my_dict}', end='\n\n')

    # - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
    my_set = set((1, 1, 1, None, False, 'spam', 'eggs', None))
    # - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
    print(f'Set: {my_set}')
    # - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
    my_set.update((my_dict.popitem(), my_dict.popitem()))
    # - Удалите один любой элемент из множества my_set.
    my_set.pop()
    # - Выведите на экран измененное множество my_set.
    print(f'Modified set: {my_set}')

if __name__ == '__main__':
    main()
