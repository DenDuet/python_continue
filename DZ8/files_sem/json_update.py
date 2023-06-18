# 📌 Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в
# JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные
# должны сохраняться.
__all__ = ['json_update']

import os.path
import json

def json_update(name: str, persid: str, level: str):
    """Функция получает данные и добавляет их в json файл"""
    # dic = json_read('data.json')
    if len(dic) > 0:
        for key, value in dic.items():
            if key == level:
                value.setdefault(persid, name)
                break
        else:
            dic.setdefault(level,{persid: name})
    else:
        dic.setdefault(level,{persid: name})
    # print(dic)
    return dic


def json_read(fname = 'data.json'):
    """Функция читает из файла данные, если есть, и возвращает словарь, либо пустой словарь"""
    if os.path.exists(fname) & len(fname) > 0:
        with open(fname,'r',encoding="UTF-8") as fjs:
            dic = json.load(fjs)
    else:
        dic = {}
    return dic
    

def write_json(dic, fname = 'data.json'):
    """Функция получает словарь с данными и записывает его в файл"""
    with open(fname,'w',encoding="UTF-8") as fjs:
        json.dump(dic, fjs)
            
            
def check_dic(dic, persid):
    """"""
    if len(dic) > 0:
        for key, value in dic.items():
            for key1, value1 in value.items():
                if key1 == persid:
                    return False
        else: 
            return True
    else:
        return True


if __name__ == '__main__':
    dic = json_read('data.json')
    print(dic)
    cont = '0'
    while cont == '0':
        name = input("Введите имя: ")
        while True:
            persid = str(input("Введите идентификатор: "))
            if check_dic(dic, persid):
                break 
        while True:
            level = int(input("Введите уровень доступа (1..7): "))
            if 0 < level < 8:
                break
        # print(name, persid, level)
        dic = json_update(name, persid, str(level))
        cont = input("Продолжить? (Да - 0): ")
        # print(dic)
    write_json(dic)