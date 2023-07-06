# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import datetime
import logging as log

FORMAT = "{levelname} - {asctime}: {msg}"
log.basicConfig(format = FORMAT, style="{", filename="debug_exc.log", level = log.DEBUG, encoding="utf-8", filemode='w')

logger = log.getLogger(__name__)


from Exceptions import PositiveError

def inp_values(num: int):
    dic = {'2': 5, '3': 66}
    num_list = [2,3,4,5]
    log.debug(f"Инициализируем словарь {dic = } и список {num_list = }")
    try:
        log.debug(f"Пытаемся сложить словарь и список в новый список...")
        new_list = num_list + dic
        log.debug(f"Новый список = словарь + список = {new_list = }")
        print(new_list,num_list, dic)
    except TypeError as e:
        print("Так не работает эта штука")
        log.error("Так не работает эта штука")
        
    try:
        inp = int(num) #(input("Введите положительное число: "))        
        log.debug(f"Введено число: {inp = }")
    except ValueError as e:
        print("Нужно ввести цифрами")
        log.error("Число нужно ввести цифрами")
    try:
        if inp < 0:        
            log.error("Нужно ввести положительное число, т.е. больше нуля.")
            raise PositiveError("Нужно ввести положительное число, т.е. больше нуля.")
            
    except UnboundLocalError as e:
        log.error("Ещё нужно следить за переменными!")
        print("Ещё нужно следить за переменными!")
        
        
inp_values("5")

inp_values("gdgf")
inp_values("-5")