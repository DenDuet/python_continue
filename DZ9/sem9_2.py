# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from random import randint
from typing import Callable


def decor(func: Callable):
    MIN_NUM = 1
    MAX_NUM = 100
    MIN_COUNT = 1
    MAX_COUNT = 10
    print("decor")
    def wrapper(*args, **kwargs):
        inp_num, inp_count = args
        print(inp_num,inp_count)
        if MIN_NUM > inp_num  or inp_num > MAX_NUM:
            inp_num = randint(MIN_NUM,MAX_NUM)
            print(inp_num,inp_count)
        if MIN_COUNT > inp_count  or inp_count > MAX_COUNT:
            inp_count = randint(MIN_COUNT,MAX_COUNT)
            print(inp_num,inp_count)
        return func(inp_num,inp_count)
    return wrapper
        

@decor
def inp_numbers(number: int, count: int) -> Callable[[],None]:
    """Функция получает загаданное число (number) и кол-во попыток для отгадывания (count) и предлагает угадать число """
    print(number,count)
    def quess_number():
        for i in range(count):
            num = int(input("Введите число от 1 до 100: "))
            print(number,count)
            if num > number:
                print(f"Введенное число больше загаданного. Осталось {count-i-1} попыток.")
            elif num < number:
                print(f"Введенное число меньше загаданного. Осталось {count-i-1} попыток.")
            else:
                print(f"Вы угадали число {number}. Осталось {count-i-1} попыток.")
                break
        else: 
            print(f"Вы не угадали число {number}. Осталось {count-i-1} попыток.")
    return quess_number
    

inp_numbers(200, 21)()
