# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
from typing import Callable

def count_run(number: int):
    def deco(func: Callable):
        my_list = []
        def wrapper(*args, **kwargs):
            for i in range(number):
                result = func(*args, **kwargs)
                my_list.append(result)
            return my_list
        return wrapper
    return deco


@count_run(3)
def fuct(num: int) -> int:
    res = 1
    for i in range(1,num+1):
        res *= i
    return res


print(fuct(5))