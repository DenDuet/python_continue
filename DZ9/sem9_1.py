# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 

from random import randint
from typing import Callable


def inp_numbers(number: int, count: int) -> Callable[[],None]:
    """Функция получает загаданное число (number) и кол-во попыток для отгадывания (count) и предлагает угадать число """
    def quess_number():
        for i in range(count):
            num = int(input("Введите число от 1 до 100: "))
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
    

inp_numbers(randint(1,101), randint(1,11))()
# b = inp_numbers(randint(1,101), randint(1,11))
# print(b())

