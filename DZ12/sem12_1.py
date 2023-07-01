# 📌 Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

class Factorial:
    numbers = {}
    def __init__(self,num):
        self.storage = num
        
    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in self.numbers.items()))
        return f'Список чисел с их факториалом:\n{txt}'

    def __call__(self, value):
        res = 1
        for i in range(2,value+1):
            res = res * i
        if len(self.numbers) == self.storage:
            dic = {}
            i=0
            for k, v in self.numbers.items():
                if i>0:
                    dic.setdefault(k,v)
                i+=1
            self.numbers=dic
        self.numbers.setdefault(value, res)
        return f'Факториал числа {value} равен {res}' 

    
f = Factorial(5)
print(f(5))
print(f(2))
print(f(3))
print(f(7))
print(f(4))
print(f(8))
print(f)