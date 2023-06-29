# 📌 Дорабатываем класс прямоугольник из прошлого семинара.
# 📌 Добавьте возможность сложения и вычитания.
# 📌 При этом должен создаваться новый экземпляр
# прямоугольника.
# 📌 Складываем и вычитаем периметры, а не длинну и ширину.
# 📌 При вычитании не допускайте отрицательных значений.


class Square:
    """В классе расчитывается периметр и площадь по принятым значениям сторон."""
    def __init__(self,long,width=0):
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
        new_long = min([self.long,self.width,other.long,other.width])
        new_width = new_perim / 2 - new_long
        return Square(new_long, new_width)
        
    
if __name__ == '__main__':
    
    p = Square(2,5)
    p1 = Square(5,10)
    print(f"{p.sqr()=}, {p.perim()=}")
    print(f"{p1.sqr()=}, {p1.perim()=}")
    res_sum = p + p1
    print(f"{res_sum.long= }, {res_sum.width= }")
    res_sub = p - p1
    print(f"{res_sub.long= }, {res_sub.width= }")
    help(Square) 