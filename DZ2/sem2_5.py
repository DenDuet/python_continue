# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

import cmath
import math

print("Для уравнения вида a*x^2 + b*x + c = 0")
a: float = float(input("Введите a = "))
b: float = float(input("Введите b = "))
c: float = float(input("Введите c = "))

d: float = b**2 - 4 * a * c
print(f"Дискриминант = {d}")

if d > 0:
    print(f"Уравнение имеет 2 корня: x1 = {(-b+math.sqrt(d))/2/a} и x2 = {(-b-math.sqrt(d))/2/a}")
elif d == 0:
    print(f"Уравнение имеет 1 корень: x = {(-b)/2/a}")
elif d < 0:
    print(f"Уравнение имеет 2 корня: x1 = {(complex(-b/2/a,cmath.sqrt(d**2-4*(a*c))/2/a))} и x2 = {(complex(-b/2/a,cmath.sqrt(-(d**2-4*(a*c)))/2/a))}")
    
    