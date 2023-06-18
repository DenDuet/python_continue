# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.
__all__ = ['read_file']

import json


def read_file(fname: str='result.txt') -> list:
    """Функция получает имя текстового файла с данными и создает из них словарь, который передает в функцию создания json файла"""

    dic = {}
    with (open(fname, 'r', encoding='UTF-8')) as fnm:
        lines = fnm.readlines()
        for line in lines:
            data = line.split(" ")
            dic.setdefault(data[0].capitalize(),data[2][:-1])
    return dic
            
            
def json_file(dic: dict, fname: str='result.json'):
    """Функция получает список с данными и создает из них json файл"""
    with open(fname,'w',encoding="UTF-8") as fjs:
        json.dump(dic, fjs, indent=2, ensure_ascii=False)

                
if __name__ == '__main__':
    dic = read_file()
    # print(dic)
    json_file(dic)