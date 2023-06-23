# Решить задачи, которые не успели решить на семинаре.
# Напишите следующие функции:
#     ○ Нахождение корней квадратного уравнения
#     ○ Генерация csv файла с тремя случайными числами в каждой строке.
#     100-1000 строк.
#     ○ Декоратор, запускающий функцию нахождения корней квадратного
#     уравнения с каждой тройкой чисел из csv файла.
#     ○ Декоратор, сохраняющий переданные параметры и результаты работы
#     функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import json
import csv
import math
from random import randint
from typing import Callable


def json_write(func: Callable):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('sqr_list.json','w',encoding="utf-8") as f:
            json.dump(res,f,indent=2)
        return res
    return wrapper



def deco(func: Callable):
    def wrapper(*args, **kwargs):
        res_list = []
        res = func(*args, **kwargs)
        for a,b,c in res:
                d = b**2-4*a*c
                if a == 0:
                    a = x1 = x2 = d = None
                    print("Это было не квадратное уравнение, т.к. a=0!")
                else:    
                    if d > 0:
                        x1 = (-b-math.sqrt(d))/2/a
                        x2 = (-b+math.sqrt(d))/2/a
                    elif d == 0:
                        x1 = x2 = -b/2/a
                    else:
                        x1 = x2 = None
                res_list.append([a,b,c,d,x1,x2])
        print(res_list)
        return res_list
    return wrapper
    
@json_write
@deco
def make_csv(text: str, number: int):
    """Функция создает файл c именем text из number строк по три случайных значения в каждой строке"""
    MAX_N = 100
    MIN_N = -100 
    arg_list = []       
    with open(text, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile); 
        for i in range(number):
            arg_list.append([randint(MIN_N,MAX_N),randint(MIN_N,MAX_N),randint(MIN_N,MAX_N)])
            spamwriter.writerow(arg_list[i])
    return arg_list
            

if __name__ == "__main__":            
    make_csv('numbers.csv', randint(10,100))            
