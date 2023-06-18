# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import json
import csv
import pickle
import os


def list_dir(dir_name, dic, count) -> int:
    """Функция получает имя каталога и рекурсивно обходит его, возвращая список файлов"""
    for fname in os.listdir(dir_name):
        f = os.path.join(dir_name, fname)
        if os.path.isfile(f):
            dic.setdefault(f+" (file)", os.path.getsize(f))
            count = count + os.path.getsize(f)
        else:
            count1 = list_dir(f, dic, 0)
            dic.setdefault(f + " (dir)", count1)
            count = count + count1
            
    return count
    

def write_json(dic, fname = 'data.json'):
    """Функция получает словарь с данными и записывает его в файл json"""
    with open(fname,'w', newline='', encoding="UTF-8") as fjs:
        json.dump(dic, fjs, indent=2, sort_keys=True)
        
        
def write_csv(dic, fname = 'data.csv'):
    """Функция получает словарь с данными и записывает в файл csv"""
    with (open(fname, 'w', newline='', encoding='utf-8') as f_write):
        csv_write = csv.DictWriter(f_write, fieldnames=["name","size"], dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        dict_row = {}
        for key, value in dic.items():
            dict_row['name'] = key
            dict_row['size'] = value
            csv_write.writerow(dict_row)
            

def write_pickle(dic,fname = 'data.pickle'):
    """Функция получает словарь с данными и записывает в файл pickle"""
    with (open(fname, 'wb') as f_write):
        pickle.dump(dic, f_write)
        
        
if __name__ == '__main__':
    dic = {}
    dic.setdefault('..\DZ6' +  " (dir)", list_dir('..\DZ6', dic, 0))
    write_json(dic, 'list_dir.json')
    write_csv(dic, 'list_dir.csv')
    write_pickle(dic, 'list_dir.pickle')