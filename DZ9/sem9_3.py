# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json
from typing import Callable


def json_save(text: str, dic: dict):
    with open(text,"w",encoding="utf-8") as f:
        json.dump(dic,f)
        f.write("\n")
        

def json_read(text: str):
    # dic = {}
    with open(text,"r",encoding="utf-8") as f:
        dic = json.load(f)
    return dic


def decor(func: Callable):
    dic = json_read("save.json")
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        # for i in range(len(args)):
        #     dic.update({f"args[{i}]": args[i]})
        # dic.update({args[i]: args[i]})
        dic.update({res: args})
        dic.update({**kwargs})
        json_save("save.json",dic)
        dic.update()
    return wrapper
        
@decor
def func_sum(number: int, number2: int, *args, **kwargs) -> int:
    return number + number2


f= func_sum(18,110,a=6,b=8)
f= func_sum(4,5,c=2,d=4)
f= func_sum(18,10,w=12,f=5)

