# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.

from functools import wraps
from random import randint
from typing import Callable


def count_run(number: int = 1):
    """Функция повторяет работу number раз"""
    @wraps(count_run)
    def decor(func: Callable):
        """Функция декоратор"""
        MIN_NUM = 1
        MAX_NUM = 100
        MIN_COUNT = 1
        MAX_COUNT = 10
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(number):
                inp_num, inp_count = args
                if MIN_NUM > inp_num  or inp_num > MAX_NUM:
                    inp_num = randint(MIN_NUM,MAX_NUM)
                if MIN_COUNT > inp_count or inp_count > MAX_COUNT:
                    inp_count = randint(MIN_COUNT,MAX_COUNT)
                result = func(inp_num,inp_count)
                # print("wrapper",inp_num,inp_count)
                print(i,result())
        return wrapper
    return decor    
        
        
@count_run(1)
def inp_numbers(number: int, count: int) -> tuple:
    """Функция получает загаданное число (number) и кол-во попыток для отгадывания (count) и предлагает угадать число """
    print("inp_numbers",number,count)
    def quess_number():
        for i in range(count):
            num = int(input("Введите число от 1 до 100: "))
            if num > number:
                print(f"Введенное число больше загаданного. Осталось {count-i-1} попыток.")
            elif num < number:
                print(f"Введенное число меньше загаданного. Осталось {count-i-1} попыток.")
            else:
                print(f"Вы угадали число {number}. Осталось {count-i-1} попыток.")
                return number, count-i-1
        else: 
            print(f"Вы не угадали число {number}. Осталось {count-i-1} попыток.")
            return "-", count-i-1
    return quess_number
    

inp_numbers(randint(110,200), randint(0,21))
print(count_run.__name__, count_run.__doc__)
print(inp_numbers.__name__, inp_numbers.__doc__)