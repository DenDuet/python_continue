# 📌 Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей

import json
import os


def json_read(fname = 'data.json'):
        """Функция читает из файла данные, если есть, и возвращает словарь, либо пустой словарь"""
        if os.path.exists(fname) & len(fname) > 0:
            with open(fname,'r',encoding="UTF-8") as fjs:
                dic = json.load(fjs)
        else:
            dic = {}
        return dic


class User:
    def __init__(self,name,persid,level):
        self.name = name
        self.persid = persid
        self.level = level
        
    def __str__(self):
        return f"Пользователь {self.name}, его id = {self.persid}, его уровень {self.level}"
    
    
if __name__ == "__main__":
    dic = json_read()
    p = []
    print(dic)
    for key,value in dic.items():
        # print(key,value)
        for key1, value1 in value.items():
            # print(key1,value1)
            p.append(User(value1,key1,key))
    print(*(str(string)+"\n" for string in p))
