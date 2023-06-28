# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Birdth:
    def __init__(self,name,num_legs,wings):
        self.name = name
        self.num_legs = num_legs
        self.wings = wings
    
    def about(self):
        about = f"Привет! Меня зовут {self.name}. У меня {self.num_legs} ног(и)."
        if self.wings == "Крылья":
            about = about + " И у меня есть крылья."
        else:
            about = about + " У меня крыльев нет."
        return about
    
class Animal:
    def __init__(self,name,num_legs,tail):
        self.name = name
        self.num_legs = num_legs
        self.tail = tail
    
    def about(self):
        about = f"Привет! Меня зовут {self.name}. У меня {self.num_legs} ног(и)."
        if self.tail == "Хвост":
            about = about + " И у меня есть хвост."
        else:
            about = about + " У меня хвоста нет."
        return about
    
class Insect:
    def __init__(self,name,num_legs,tail,wings):
        self.name = name
        self.num_legs = num_legs
        self.tail = tail
        self.wings = wings
    
    def about(self):
        about = f"Привет! Меня зовут {self.name}. У меня {self.num_legs} ног(и)."
        if self.tail == "Хвост":
            about = about + " И у меня есть хвост."
        else:
            about = about + " У меня хвоста нет."
        if self.wings == "Крылья":
            about = about + " Также у меня есть крылья."
        else:
            about = about + " И крыльев нет."
        return about
    

b = Birdth("Птичка",2,"Крылья")
b1 = Birdth("Птичка 2",2,"Нет")
print(" ", b.about(), "\n ", b1.about())

с = Animal("Собака",4,"Хвост")
с2 = Animal("Собака 2",4,"Нет хвоста")
с1 = Animal("Кот 2",4,"Хвост")
print(" ", с.about(), "\n ", с1.about(), "\n ", с2.about())

d = Insect("Шмель",8,"Нет","Крылья")
d1 = Insect("Муха",6,"Хвост","Крылья")
d2 = Insect("Комар",6,"Нет","Нет")
print(" ", d.about(), "\n ", d1.about(), "\n ", d2.about())