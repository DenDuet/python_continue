# ✔ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


def filename(text):
    """Функция делит строку text на несколько частей и возвращает кортеж из данных. """
    *path, name = text.split('/') 
    path = '/'.join(path)
    name, ex = name.split(".")
    path_tup = (path, name, ex,)
    return path_tup
    
tup = filename("c:/windows/temp/tmp/exec.bin")
print(f"\nПуть до файла: {tup[0]} \nимя файла: {tup[1]} \nрасширение файла: {tup[2]} \n\nКортеж: {tup}\n")