# Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр
# и площадь.
# 📌 Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Square:
    
    def __init__(self,long,width=0):
        self.long = long
        if width == 0:
            self.width = long
        else:
            self.width = width
    
        
    def sqr(self):
        return self.long * self.width
    
    def perim(self):
        return 2 * (self.long + self.width)
    
p = Square(10)
print(f"{p.sqr()=}, {p.perim()=}")

p = Square(10,20)
print(f"{p.sqr()=}, {p.perim()=}")