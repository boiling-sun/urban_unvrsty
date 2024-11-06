from math import inf

def divide(first, second):
    """
    Возвращает результат деления first на second, но когда в second записан 0 - возвращает бесконечность.
    """
    try:
        return first / second
    except ZeroDivisionError:
        return inf