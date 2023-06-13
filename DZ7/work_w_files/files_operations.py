# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.
__all__ = ['files_operations']


def files_operations(name1: str, name2: str, name3: str):
    """Функция получает на вход имена файлов. В первом содержатся цифры (int | float), 
    во втором имена, после преобразования, данные помещаются в третий файл """    
    with (open(name1, "r", encoding="UTF-8") as fnum,
         open(name2, "r", encoding="UTF-8") as fname,
         open(name3, "w", encoding="UTF-8") as result):
        line = len(fnum.readlines())
        lines = len(fname.readlines())

        if line > lines:
            count = line
        else:
            count = lines
        fnum.seek(0)
        fname.seek(0)
        numbers = fnum.readline()
        names = fname.readline()     
            
        while count > 0:
            numbers = numbers.rstrip('\n')
            names = names.rstrip('\n')
            number = numbers.split(" ")
            num = int(number[0]) * float(number[2])
            if num < 0:
                result.write(f"{names.lower()} -> {abs(num)}\n")
            else:
                result.write(f"{names.upper()} -> {num:.0f}\n")
            count -=1
            line-=1
            lines-=1
            if line == 0:
                fnum.seek(0)
                line = len(fnum.readlines())
                fnum.seek(0)
            numbers = fnum.readline()
            if lines == 0:
                fname.seek(0)
                lines = len(fname.readlines())
                fname.seek(0)
            names = fname.readline()


if __name__ == "__main__":
    files_operations("z1.txt", "names.txt", "result.txt")