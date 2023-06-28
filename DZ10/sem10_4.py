# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
#   ○ шестизначный идентификационный номер
#   ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

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
    
    
class Stuff(Person):
    def __init__(self, id, *args, **kwargs):
        CALC_LEVEL = 7
        super().__init__(*args, **kwargs)
        self.id = id
        sum = 0
        for i in range(len(id)):
            sum = sum + int(id[i])
        self.code = sum % CALC_LEVEL
        
        
if __name__ == '__main__':
    p=Stuff("625452","николай","петров","семенович",20,"125-487")
    # print(f"{p.__age}")
    print(f"{p.get_age()=}, {p.tel=}, {p.name=}, {p.full_name()=}")
    p.birthday()
    print(f"{p.id=}, {p.code=}")
    