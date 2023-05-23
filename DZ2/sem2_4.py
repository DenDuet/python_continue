# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math 
from decimal import Decimal
from decimal import getcontext

MIN_DIAMETER = 1
MAX_DIAMETER = 1000

while True:
    diam = int(input("Введите диаметр (1-1000): "))
    if MAX_DIAMETER >= diam > MIN_DIAMETER:
        break
    
getcontext().prec = 50

print(f"Площадь круга c диаметром {diam} у.е. = {round((Decimal(math.pi) * diam**2 / 4), 42)}")
print(f"Площадь окружности c диаметром {diam} у.е. = {round((Decimal(math.pi) * diam), 42)}")
