def divide(first, second):
    """
    возвращает результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.
    """
    try:
        return first / second
    except ZeroDivisionError:
        return 'Ошибка'