# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# 📌 Используйте декораторы свойств.

class Square:
    """В классе расчитывается периметр и площадь по принятым значениям сторон."""
    def __init__(self,long,width=0):
        """В функции инициализируется новый элемент."""
        self._long = long
        if width == 0:
            self._width = long
        else:
            self._width = width
            
    def __str__(self):
        return f"Прямоугольник со сторонами {self._long} {self._width}"
    
    @property
    def long(self):
        return self._long

    @property
    def width(self):
        return self._width
    
    @long.setter
    def long(self, value):
        if value > 0:
            self._long = value
        else:
            raise ValueError(f"Длина {value} должна быть больше 0.")
        
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError(f"Ширина {value} должна быть больше 0.")        
        
    
if __name__ == '__main__':
    
    p = Square(2,5)
    p1 = Square(5,-10)
    print(p, "\n", p.long, p.width)
    print(p1, "\n",  p1.long, p1.width)
    p1.width = 10
    print(p1.width)
    # p1.width = -10
    print(p1.width)    
 