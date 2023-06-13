# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
__all__ = ['randname']

from random import randint


def randname() -> str:
    """Функция создает случайное имя"""
    VOW1 = 1
    VOW2 = 2
    x: int = randint(4,7)
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
            return name[0].upper()+name[1:]

    
if __name__ == "__main__":
    with (open("names.txt","a",encoding="UTF-8")) as f:
        f.write(randname()+"\n")