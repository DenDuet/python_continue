# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции. 
__all__ = ['randnum']

from random import randint
import random
from sys import argv

def randnum() -> int | float:
    """Функция генерирует 2 числа, одно int, другое float"""
    MIN_NUM = -1000
    MAX_NUM = 1000
    x :int = randint(MIN_NUM,MAX_NUM)
    y :float = random.uniform(MIN_NUM*0.01, MAX_NUM*0.01)
    return x, y

if __name__ == '__main__':
    if len(argv) > 3:
        with open(argv[1], "a", encoding="UTF-8") as f:
            for i in range(int(argv[2])):
                x, y = randnum()
                f.write(f"{x} | {y}\n")
    else:
        with open("z1.txt", "a", encoding="UTF-8") as f:
            for i in range(10):
                x, y = randnum()
                f.write(f"{x} | {y}\n")
