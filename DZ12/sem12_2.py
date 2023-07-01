# Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

import json 

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
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('result.json','w',encoding="utf-8") as f_json:
            json.dump(self.numbers,f_json, indent=2)
            print(f_json)
            # self.f_json.close()
            # self.f_json = None

if __name__ == "__main__":    
    with Factorial(5) as f:
        print(f(1))
        print(f(2))
        print(f(3))
        print(f(4))
        print(f(5))
        print(f(6))
        print(f(7))
        print(f(8))        
        print(f)