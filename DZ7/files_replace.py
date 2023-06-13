# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# __all__ = ['files_replace']

import os
import work_w_files.file_gen as fgen


def create_files(param: list):
    '''Функция принимает значения: расширение файла и количество файлов списком и вызывает функцию 
    files_gen для создания этих файлов''' 
    if len(param) > 0:
        for i in range(len(param)):
            fgen.files_gen(param[i][0],param[i][1], False)
            

def f_replace(f_name: str='test', number: int=2, ext_s: str='txt', ext_d: str='bin', rng: list=[1,3]):
    list_dir = os.listdir()
    print(list_dir)

    for i in range(len(list_dir)):
            if list_dir[i][-3:] == ext_s:
                name = list_dir[i][rng[0]:rng[1]+1] + f_name + f'{i:0{number}}'+'.'+ext_d
                print(list_dir[i], name)
                os.replace(list_dir[i], name)    
                
    
if __name__ == '__main__':
    # param = [['txt',3], ['bin', 2], ['doc', 5], ['ogg', 3], ['avi', 2], ['mov', 3], ['mpg', 3], ['mp3', 2], ['jpg', 3], ['png', 3], ['gif', 3]]
    param = [['txt',3], ['bin', 2], ['doc', 5]]

    # dirs = [['text', ['doc','txt']], ['music', ['mp3','ogg']], ['video', ['avi','mov','mpg']], ['image', ['jpg','png','gif']]]
    if not os.path.exists('files'):
        os.mkdir('files')
    create_files(param)
    os.chdir('files')
    f_replace()
    f_replace('doc',3,'doc','fff',[2,5])
    f_replace('rrr',2,'bin','bbb',[0,1])
    # mk_dirs(dirs)