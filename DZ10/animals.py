# Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс
# Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.


from datetime import datetime


class Animal:
    def __init__(self,name,num_legs,birth_year):
        self.name = name
        self.num_legs = num_legs
        self.birthday = birth_year
    
    def about(self):
        about = f"Привет! Меня зовут {self.name}. У меня {self.num_legs} ног(и). Мне {datetime.today().year-self.birthday} года(год)."
        return about
    
class Dog(Animal):
    def __init__(self,name,num_legs,birth_year,tail,say):
        super().__init__(name,num_legs,birth_year)
        self.tail = tail
        self.says = say
    
    def say(self):
        return self.says        
    
    def about(self):
        about = f"Привет! Меня зовут {self.name}. У меня {self.num_legs} ног(и). Мне {datetime.today().year-self.birthday} года(год)."
   
        if self.tail == "Хвост":
            about = about + " У меня есть хвост."
        else:
            about = about + " У меня хвоста нет."
        about = about + f" Я умею говорить {self.say()}"
        return about
    
class Cat(Animal):
    def __init__(self,name,num_legs,birth_year,tail,wool,say):
        super().__init__(name,num_legs,birth_year)
        self.tail = tail
        self.wool = wool
        self.says = say
    
    def say(self):
        return self.says        
    
    def about(self):
        about = f"Привет! Меня зовут {self.name}. У меня {self.num_legs} ног(и). Мне {datetime.today().year-self.birthday} года(год)."

        if self.tail == "Хвост":
            about = about + " У меня есть хвост."
        else:
            about = about + " У меня хвоста нет."
        if self.wool == "Шерсть":
            about = about + " У меня есть шерсть."
        else:
            about = about + " У меня шерсти нет."
        about = about + f" Я умею говорить {self.say()}"
        return about    
    

class Bird(Animal):
    def __init__(self,name,num_legs,birth_year,wings,say):
        super().__init__(name,num_legs,birth_year)
        self.wings = wings
        self.says = say
    
    def say(self):
        return self.says
    
    def about(self):
        about = f"Привет! Меня зовут {self.name}. У меня {self.num_legs} ног(и). Мне {datetime.today().year-self.birthday} года(год)."
        if self.wings == "Крылья":
            about = about + " И у меня есть крылья."
        else:
            about = about + " У меня крыльев нет."
        about = about + f" Я умею говорить {self.say()}"
        return about
    
    
class Fish(Animal):
    def __init__(self,name,num_legs,birth_year,fin,tail,say):
        super().__init__(name,num_legs,birth_year)
        self.fin = fin
        self.tail = tail
        self.says = say
        
    def say(self):
        return self.says        
    
    def about(self):
        about = f"Привет! Меня зовут {self.name}."
        if self.num_legs > 0:
            about = about + f" У меня {self.num_legs} ног(и)."
        else:
            about = about + " У меня нет ног."        
        if self.tail == "Хвост":
            about = about + " У меня есть хвост."
        else:
            about = about + " У меня хвоста нет."
        if self.fin == "Плавники":
            about = about + " Также у меня есть плавники."
        else:
            about = about + " А плавников нет."
        about = about + f" Я умею говорить {self.say()}"
        return about
    

if __name__ == "__main__":
    с = Dog("Лабрадор",4,2010,"Хвост","Гав-гав")
    с2 = Dog("Такса",4,1999,"Нет хвоста","Гав-гав-гав")
    с1 = Cat("Кот",4,2022,"Нет хвоста","Шерсть","Мяу")
    print(" ", с.about(), "\n ", с1.about(), "\n ", с2.about())

    с = Bird("Воробей",2,1998, "Крылья", "Чирик-Чирик")
    с2 = Bird("Чиж",2,2011, "Крылья", "Жжжжик")
    с1 = Bird("Сорока",2,2021, "Крылья", "Чик-Чик")
    print(" ", с.about(), "\n ", с1.about(), "\n ", с2.about(), с2.say())

    с = Fish("Угорь",0,2018, "Нет плавников", "Хвост", "но меня никто не слышит...")
    с1 = Fish("Карась",0,2021, "Плавники", "Хвост", "но меня никто не слышит...")
    с2 = Fish("Щука",0,2022, "Плавники", "Хвост", "но меня никто не слышит...")
    print(" ", с.about(), "\n ", с1.about(), "\n ", с2.about(), с2.say())