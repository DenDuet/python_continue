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

from animals import *
# from animals import Cat
# from animals import Bird
# from animals import Fish



class Zoo(Dog,Cat,Bird,Fish):
    
    # def __init__(self,type,name,num_legs,birth_year,tail=None,say=None,wool=None,wings=None,fin=None):
    def __init__(self, type, *args, **kwargs):
        if (type==Dog):
            Dog.__init__(self,*args,**kwargs)
        elif(type==Cat):
            Cat.__init__(self,*args,**kwargs)
        elif(type==Bird):
            Bird.__init__(self,*args,**kwargs)
        elif(type==Fish):
            Fish.__init__(self,*args,**kwargs)
        # else:
        #     print("Неправильно указан тип животного")        

        # if (type==Dog):
        #     Dog.__init__(name,num_legs,birth_year,tail,say)
        # elif(type==Cat):
        #     Cat.__init__(name,num_legs,birth_year,tail,wool,say)
        # elif(type==Bird):
        #     Bird.__init__(name,num_legs,birth_year,wings,say)
        # elif(type==Fish):
        #     Fish.__init__(name,num_legs,birth_year,fin,tail,say)
        # else:
        #     print("Неправильно указан тип животного")        
       
        
# zoo1 = Zoo(Dog,"Лабрадор",4,2010,"Хвост","Гав-гав")

# с2 = Dog("Такса",4,1999,"Нет хвоста","Гав-гав-гав")
zoo2 = Zoo(type=Cat,name="Мурка",num_legs=4,birth_year=2022,tail="Нет хвоста",wool="Шерсть",say="Мяу")
# print(с2.about())
# print(zoo1.about(), zoo1)
print(zoo2.about(), zoo2)
# 

# zoo3 = Zoo("Bird",2,1998, "Крылья", "Чирик-Чирик")
# print(zoo3.about(), zoo3)
# с2 = Birdth("Чиж",2,2011, "Крылья", "Жжжжик")
# с1 = Birdth("Сорока",2,2021, "Крылья", "Чик-Чик")
# print(" ", с.about(), "\n ", с1.about(), "\n ", с2.about(), с2.say())

# zoo4 = Zoo("Fish",0,2018, "Нет плавников", "Хвост", "но меня никто не слышит...")
# print(zoo4.about(), zoo4)
# с1 = Fish("Карась",0,2021, "Плавники", "Хвост", "но меня никто не слышит...")
# с2 = Fish("Щука",0,2022, "Плавники", "Хвост", "но меня никто не слышит...")
# print(" ", с.about(), "\n ", с1.about(), "\n ", с2.about(), с2.say())