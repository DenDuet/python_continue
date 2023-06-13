# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
__all__ = ['file_gen']

from random import randint
import os
import shutil

MIN_LEN = 6
MAX_LEN = 30
MIN_BYTES = 256
MAX_BYTES = 4096
FILES_NUMBER = 42


def randname(min_len: int=MIN_LEN, max_len: int=MAX_LEN) -> str:
    """Функция создает случайное имя"""
    VOW1 = 1
    VOW2 = 2
    x: int = randint(min_len, max_len)
    vowel = "aeiouy"
    
    while True:
        name = ""
        if x < 4:
            vow = VOW1
        else:
            vow = VOW2

        for i in range(x):
            y = randint(97,122)
            if chr(y) in vowel:
                vow -= 1
            name = name + chr(y)
        if vow <= 0:
            return name


def files_gen(extention: str, files_number: int= FILES_NUMBER, del_cat: bool=True, min_len: int=MIN_LEN, max_len: int=MAX_LEN, min_bytes: int=MIN_BYTES, max_bytes: int=MAX_BYTES):
    """Функция создаёт файлы с указанным расширением."""
    if del_cat:
        if not os.path.exists("files"):
            os.mkdir("files")
        else:
            shutil.rmtree("files")
            os.mkdir("files")
        
    for i in range(files_number):
        name = randname(min_len, max_len)
        name = "files\\" + name + str(i) + "." + extention
        if os.path.exists(name):
            name = name + "_"
        with (open(name, "wb") as f):
            # filelen = randint(min_bytes,max_bytes)
            data = bytes(randint(0,255) for i in range(randint(min_bytes,max_bytes)))
            f.write(data)
 
    
if __name__ == "__main__":    
    # files_gen("txt", 24, 10, 20, 256, 6000)
    files_gen("txt")