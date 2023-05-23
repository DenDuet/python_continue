# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
import math 

str = input("Введите первую дробь вида a/b: ")
a,b = str.split('/')
a = int(a)
b = int(b)

str1 = input("Введите вторую дробь вида c/d: ")
c,d = str1.split('/')
c = int(c)
d = int(d)

print("")
if b == d:
    nod = math.gcd(a+c,b)
    if nod != 0:
        print(f"Сумма дробей = {int((a+c)/nod)}/{int(b/nod)}")
    else:
        print(f"Сумма дробей = {(a+c)}/{b}")
else:
    nod = math.gcd((a*d+c*b),b*d)
    if nod != 0:
        print(f"Сумма дробей = {int((a*d+c*b)/nod)}/{int(b*d/nod)}")
    else:
        print(f"Сумма дробей = {(a*d+c*b)}/{b*d}")

nod = math.gcd(a*c,b*d)
if nod !=0:
    print(f"Произведение дробей = {int(a*c/nod)}/{int(b*d/nod)}")
else:
    print(f"Произведение дробей = {a*c}/{b*d}")

print("")
print(f"Сумма дробей с функцией Fraction = {Fraction(a,b) + Fraction(c,d)}")
print(f"Произведение дробей с функцией Fraction = {Fraction(a,b) * Fraction(c,d)}")
print("")
