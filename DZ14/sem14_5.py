# 📌 На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# 📌 Напишите 3-7 тестов unittest для данного класса.

import unittest


class Square:
    """В классе расчитывается периметр и площадь по принятым значениям сторон."""

    def __init__(self, long, width=0):
        """В функции инициализируется новый элемент."""
        self.long = long
        if width == 0:
            self.width = long
        else:
            self.width = width

    def sqr(self):
        """Функция расчитывает площадь прямоугольника."""
        return self.long * self.width

    def perim(self):
        """Функция расчитывает периметр прямоугольника."""
        return 2 * (self.long + self.width)

    def __add__(self, other):
        """Функция суммирует элементы класса."""
        new_perim = self.perim() + other.perim()
        new_long = self.long
        new_width = new_perim / 2 - new_long
        return Square(new_long, new_width)

    def __sub__(self, other):
        """Функция вычитает элементы класса."""
        new_perim = abs(self.perim() - other.perim())
        new_long = min([self.long, self.width, other.long, other.width])
        new_width = new_perim / 2 - new_long
        return Square(new_long, new_width)


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Square(2, 5)
        self.rect2 = Square(2, 2)

    def test_method(self):
        self.assertEqual(self.rect2.long, 2)
        self.assertEqual(self.rect2.width, 2)

    def test_square(self):
        self.assertEqual(self.rect1.sqr(), 10)

    def test_perimetr(self):
        self.assertEqual(self.rect2.perim(), 8)

    def test_sub(self):
        self.assertEqual((self.rect1 - self.rect2).perim(), 6)



if __name__ == "__main__":
    unittest.main(verbosity=2)