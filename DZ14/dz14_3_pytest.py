# 📌 Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

import pytest

def inp_num(inp):
    try:
        num = int(inp)
        return num
    except ValueError as e:
            try:
                num = float(inp) # Эта строка переводит число 5.15 в число 5! и выдает ошибку
                return num
            except ValueError as e:
                return False
                

def test_int():
    assert inp_num(7) == 7

def test_method_float():
    assert inp_num(5.15) == 5.15        
    
def test_method_skip():
    assert inp_num("Text") == False

if __name__ == '__main__':
    pytest.main(["-v"])

    # num = inp_num(input("Введите целое или вещественное число: "))
    # print(num)
        