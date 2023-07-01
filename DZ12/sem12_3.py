# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.
import json

class Factorial:
    numbers = {}
    def __init__(self, num):
          self.num = num

    def __call__(self, stop, start=1, step=1):
        res = 1
        for i in range(1,start):
            res = res * i
        j = 1
        for i in range(start,stop+1):
            res = res * i
            if j > 1:
                j -= 1
            else:
                j = step
                yield res
                
if __name__ == "__main__":    
    f = Factorial(5)
    print(f(5))
    print(*f(5))
    print(*f(8,2,1))
    print(*f(8,3,2))
