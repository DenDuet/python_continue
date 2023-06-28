# Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании
# экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину
# окружности и её площадь.


import math


class Circle():
    def __init__(self, radius: float):
        self.radius = radius
        
    def long_circle(self):
        return 2*math.pi*self.radius
    
    def area(self):
        return math.pi*self.radius**2
    
    
p = Circle(10)
print(f"{p.long_circle()=}, {p.area()=}")

    