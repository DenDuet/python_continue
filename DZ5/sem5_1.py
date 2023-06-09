# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
# хранятся в кортеже как значения второго ключа.


def ex(text) -> dict:
    """Функция разделяет строку text на части и составляет из них словарь с 2мя парами ключ: значение."""
    a, b, c, *d = text.split("/")
    dic = {}
    dic.setdefault(b, a)
    dic.setdefault(c, d)
    return dic
    
    
text = input("Введите строку из 4 и более целых чисел, разделенных \"/\": ")
dic = ex(text)
print(dic)