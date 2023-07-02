# 📌 Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

import unittest

class TestCaseName(unittest.TestCase):
    def test_method_int(self):
        self.assertEqual(inp_num(7), 7)
        
    def test_method_float(self):
        self.assertEqual(inp_num(5.15), 5.15)        
    
    def test_method_skip(self):
        self.assertEqual(inp_num("Text"), False)

def inp_num(inp):
    """
    Функция получает значение inp и переводит его в int или float
    >>> inp_num(5)
    Вы ввели целое число: 5
    5
    >>> inp_num(5.15)
    Введенное значение: 5.15 - это не целое число
    Вы ввели вещественное число: 5.15
    5.15
    >>> inp_num("text")
    Введенное значение: text - это не целое число
    Введенное значение: text - это не число
    """
    try:
        num = float(inp)
        return num
    except ValueError as e:
            try:
                num = int(inp)
                return num
            except ValueError as e:
                return False
                

if __name__ == '__main__':
    unittest.main(verbosity=2)

    # import doctest
    # doctest.testmod(verbose=True)

#     num = inp_num(input("Введите целое или вещественное число: "))
        