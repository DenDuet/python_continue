# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import datetime
import logging as log

FORMAT = "{levelname} - {asctime}: {msg}"
log.basicConfig(format = FORMAT, style="{", filename="info_factorial.log", level = log.INFO, encoding="utf-8", filemode='w')
logger = log.getLogger(__name__)

class Factorial:
    numbers = {}
    def __init__(self,num):
        self.storage = num
        
    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.numbers.items()))
        log.info(f"Список чисел с их факториалом:\n{txt}")
        return f'Список чисел с их факториалом:\n{txt}'

    def __call__(self, value):
        res = 1
        for i in range(2,value+1):
            res = res * i
        if len(self.numbers) == self.storage:
            dic = {}
            i=0
            for k, v in self.numbers.items():
                if i>0:
                    dic.setdefault(k,v)
                i+=1
            self.numbers=dic
        self.numbers.setdefault(value, res)
        log.info(f"Факториал числа {value} равен {res}")
        return f'Факториал числа {value} равен {res}' 

    
f = Factorial(5)
print(f(5))
print(f(2))
print(f(3))
print(f(7))
print(f(4))
print(f(8))
print(f)