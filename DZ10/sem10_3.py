# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, name, family, f_name, age, tel):
        self.name = name
        self.family = family
        self.f_name = f_name
        self.__age = age
        self.tel = tel
    
    def birthday(self):
        self.__age +=1
        return self.__age
    
    def get_age(self):
        return self.__age
        
    def full_name(self):
        return f"{self.family.capitalize()} {self.name.capitalize()} {self.f_name.capitalize()}"
    
    
p=Person("николай","петров","семенович",20,"125-487")
# print(f"{p.__age}")
print(f"{p.get_age()=}, {p.full_name()=}")
p.birthday()
print(f"{p.get_age()=}")


