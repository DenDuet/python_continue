# 📌 Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# 📌 Например отлавливаем ошибку деления на ноль.


import logging as log

log.basicConfig(filename="error.log", level = log.ERROR, encoding="utf-8", filemode='a')

def sub(a: float, b: float) -> float:
    try: 
        c = a / b
        return c
    except ZeroDivisionError as e:
        log.error(f'Ошибка деления на 0.')

c = sub(2.3, 5.6)
print(c)
c = sub(6,0)
print(c)