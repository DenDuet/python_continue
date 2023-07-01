# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import csv

class Range:
    def __init__(self, min_value: int = None, max_value: int =None):
        self.min_value = min_value
        self.max_value = max_value
        
    def __set_name__(self, owner, name):
        self.param_name = '_' + name
        
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
        
    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    
    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}')
        if self.max_value is not None and value >= self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}')

class Student:
    point = Range(2, 5+1)
    test = Range(0,100+1)
    
    def __init__(self,name: str, point, test):
        if name.replace(" ", "").isalpha():
            self.name = name.capitalize()
        self.point = point
        self.test = test
        self.points = []
        self.tests = []
        self.objects = []
    
    def make_right(self,objects):
        for subj, point, test in objects:
            self.objects.append(subj)
            self.points.append(point)
            self.tests.append(test)
        return self
    
    def avg_points(self):
        sum = 0
        for i in self.points:
            sum = sum + int(i)
        return sum / len(self.points)
    
    def avg_tests(self):
        sum = 0
        for i in self.tests:
            sum = sum + int(i)
        return sum / len(self.tests)
    
    def __enter__(self):
        with open('object_w_points.csv','r',encoding="utf-8") as f_csv:
            objects = csv.reader(f_csv)
            objects=list(objects)
            self.make_right(objects)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
            return self
            
    def __str__(self):
        str_ = f"Вот такая ведомость у студента: {self.name}\n\n"
        str_ = str_ + "  Предмет     Оценка       Тест\n"
        for i in range(len(self.objects)):
            str_ = str_ + f"{self.objects[i]:<10}       {self.points[i]:<8}   {self.tests[i]:<3}\n"
        return str_

if __name__ == "__main__":    
    with Student("алекс",5,100) as f:
        # print(f"{f.name=}")
        # print(f"{f.objects}")
        # print(f"{f.tests = }")
        # print(f"{f.points =}")
        print(f"{f}")
        print(f"Средняя оценка: {f.avg_points()}")
        print(f"Средний балл по тестам: {f.avg_tests()}")

    # with Student("ал1екс",6,101) as f:
        # print(f"{f.name=}")