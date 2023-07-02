# 📌 Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

def inp_num(inp):
    """
    Функция получает значение inp и переводит его в int или float
    >>> inp_num(5)
    5
    >>> inp_num(5.15)
    5.15
    >>> inp_num("text")
    False
    """
    try:
        num = int(inp)
        return num
    except ValueError as e:
        try:
                num = float(inp) # Тест эту строку inp_num(5.15) упорно переводит как (5) и выводит ошибку, если поменять 20 и 24 строки, то функция будет переводить 5 в 5.0...
                return num
        except ValueError as e:
                return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
#     print(inp_num(input("Введите целое или вещественное число: ")))
        