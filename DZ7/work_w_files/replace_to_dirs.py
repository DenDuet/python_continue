# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
__all__ = ['replace_to_dirs']

import os
import file_gen as fgen


def create_files(param: list):
    '''Функция принимает значения: расширение файла и количество файлов списком и вызывает функцию 
    files_gen для создания этих файлов''' 
    if len(param) > 0:
        for i in range(len(param)):
            fgen.files_gen(param[i][0],param[i][1], False)


def mk_dirs(dirs: list):
    """Функция создает каталоги и переносит в них файлы, согласно списку dirs"""
    list_dir = os.listdir()
    print(list_dir)
    for cat,ext in dirs:
        if not os.path.exists(cat):
            os.mkdir(cat)
        for file in list_dir:
            if file[-3:] in ext:
                os.replace(file, os.path.join(cat,file))


if __name__ == '__main__':
    param = [['txt',3], ['bin', 2], ['doc', 5], ['ogg', 3], ['avi', 2], ['mov', 3], ['mpg', 3], ['mp3', 2], ['jpg', 3], ['png', 3], ['gif', 3]]
    dirs = [['text', ['doc','txt']], ['music', ['mp3','ogg']], ['video', ['avi','mov','mpg']], ['image', ['jpg','png','gif']]]
    if not os.path.exists('files'):
        os.mkdir('files')
    create_files(param)
    os.chdir('files')
    mk_dirs(dirs)