# Решить задачи, которые не успели решить на семинаре.
# 📌 Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
# 📌 Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

import datetime
from animals import Dog
from animals import Cat
from animals import Bird
from animals import Fish

class Fishs:
    """Класс заглушка, чтобы проверить строку 39"""
    def __init__(self):
        self.name = self
    def about(self):
        return self
    def say(self):
        return self

class Zoo:
    def __init__(self,type_animal,*args,**kwargs):
        self.type_animal = type_animal
        if (type_animal==Dog):
            self.animal = self.make_dog(**kwargs)
        elif(type_animal==Cat):
            self.animal = self.make_cat(**kwargs)
        elif(type_animal==Bird):
            self.animal = self.make_bird(**kwargs)
        elif(type_animal==Fish):
            self.animal = self.make_fish(**kwargs)
        else:
            print("Неправильно указан тип животного") 
            exit(0)          

    def about(self):
        about = f"Привет! Меня зовут {self.name}. У меня {self.num_legs} ног(и). Мне {datetime.today().year-self.birthday} года(год)."
   
        if self.tail == "Хвост":
            about = about + " У меня есть хвост."
        else:
            about = about + " У меня хвоста нет."
        about = about + f" Я умею говорить {self.say()}"
        return about

    def make_dog(self,name,num_legs,birth_year,tail,say):
        return Dog(name,num_legs,birth_year,tail,say)         
    
    def make_cat(self,name,num_legs,birth_year,tail,wool,say):
        return Cat(name,num_legs,birth_year,tail,wool,say)     
    
    def make_bird(self,name,num_legs,birth_year,wings,say):
        return Bird(name,num_legs,birth_year,wings,say)
    
    def make_fish(self,name,num_legs,birth_year,fin,tail,say):
        return Fish(name,num_legs,birth_year,fin,tail,say)
      
        
zoo1 = Zoo(type_animal=Dog,name="Лабрадор",num_legs=4,birth_year=2010,tail="Хвост",say="Гав-гав")
print(zoo1.animal.about(), zoo1.animal.say())
zoo2 = Zoo(type_animal=Cat,name="Мурка",num_legs=4,birth_year=2022,tail="Нет хвоста",wool="Шерсть",say="Мяу")
print(zoo2.animal.about(), zoo2.animal.say())
zoo3 = Zoo(type_animal=Bird,name="Чиж",num_legs=2,birth_year=2011, wings="Крылья", say="Жжжжик")
print(zoo3.animal.about(), zoo3.animal.say())
zoo4 = Zoo(type_animal=Fish,name="Щука",num_legs=0,birth_year=2022, fin="Плавники", tail="Хвост", say="но меня никто не слышит...")
print(zoo4.animal.about(), zoo4.animal.say())
# Это строки для проверки отработки неправильного класса
zoo5 = Zoo(type_animal=Fishs,name="Щука",num_legs=0,birth_year=2022, fin="Плавники", tail="Хвост", say="но меня никто не слышит...")
print(zoo5.animal.about(), zoo5.animal.say())

