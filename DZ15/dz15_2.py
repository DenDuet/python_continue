# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import datetime
import logging as log

FORMAT = "{levelname} - {asctime}: {msg}"
log.basicConfig(format = FORMAT, style="{", filename="debug_dz15_2.log", level = log.DEBUG, encoding="utf-8", filemode='w')
logger = log.getLogger(__name__)

import json
import os


def json_read(fname = 'data.json'):
        """Функция читает из файла данные, если есть, и возвращает словарь, либо пустой словарь"""
        if os.path.exists(fname) & len(fname) > 0:
            with open(fname,'r',encoding="UTF-8") as fjs:
                dic = json.load(fjs)
                log.debug(f"Открыли файл {fname} на чтение и прочитали словарь:\n{dic} ")
        else:
            dic = {}
            log.debug(f"Открыли файл {fname} на чтение. Он оказался пустой, поэтому словарь тоже пустой:\n{dic} ")
        return dic


class User:
    def __init__(self,name,persid,level):
        self.name = name
        self.persid = persid
        self.level = level
        log.debug(f"Инициализировали нового User {self.name}, его id = {self.persid}, его уровень {self.level}")
        
    def __str__(self):
        log.debug(f"Вывод пользователья {self.name}, его id = {self.persid}, его уровень {self.level}")
        return f"Пользователь {self.name}, его id = {self.persid}, его уровень {self.level}"
    
    
if __name__ == "__main__":
    log.debug(f"Начинаем работу... читаем словарь.")
    dic = json_read()
    p = []
    print(dic)
    for key,value in dic.items():
        # print(key,value)
        for key1, value1 in value.items():
            # print(key1,value1)
            p.append(User(value1,key1,key))
    print(*(str(string)+"\n" for string in p))
