# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ним
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.

from Exceptions import PositiveError

def inp_values():
    dic = {'2': 5, '3': 66}
    num_list = [2,3,4,5]
    try:
        new_list = num_list + dic
        print(new_list,num_list, dic)
    except TypeError as e:
        print("Так не работает эта штука")
        
    try:
        inp = int(input("Введите положительное число: "))        
    except ValueError as e:
        print("Нужно ввести цифрами")
    try:
        if inp < 0:        
            raise PositiveError("Нужно ввести положительное число, т.е. больше нуля.")
    except UnboundLocalError as e:
        print("Ещё нужно следить за переменными!")
        
        
inp_values()