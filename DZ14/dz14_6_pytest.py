# 📌 Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

import pytest
     
        
def factorial(n):
    """Возвращает факториал числа n, которое является числом >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    Кроме того, число не должно быть слишком большим:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math

    if not n >= 0:
            raise ValueError("n must be >= 0")
    if math.floor(n) != n:
            raise ValueError("n must be exact integer")
    if n+1 == n: # перехватываем значения типа 1e300
            raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

def test_method_int():
        assert factorial(6) == 720

def test_method_int_range():
        assert [factorial(n) for n in range(6)] == [1, 1, 2, 6, 24, 120]
        
def test_method_otr():
        # self.assertRaisesRegex(ValueError,factorial(-1), 'n must be >= 0')        
        with pytest.raises(ValueError):
            factorial(-1)
    
def test_method_big():
        with pytest.raises(OverflowError):
            factorial(1e100)

def test_method_float():
        with pytest.raises(ValueError):
            factorial(30.1)


if __name__ == "__main__":
    pytest.main(["-v"])