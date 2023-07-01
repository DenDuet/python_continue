# 📌 Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# 📌 добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

import json
import os
from sem13_3 import LevelError, AccessError

class Access:
    def __init__(self):
        self.FILE_NAME = 'data.json'
        self.dic = self._json_read()
        self.users = self._start_auth(self.dic)
        self.print_users()
        self.log_in = []
        
    def _json_read(self):
        """Функция читает из файла данные, если есть, и возвращает словарь, либо пустой словарь"""
        if os.path.exists(self.FILE_NAME) & len(self.FILE_NAME) > 0:
            with open(self.FILE_NAME,'r',encoding="UTF-8") as fjs:
                dic = json.load(fjs)
        else:
            dic = {}
        return dic
    
    def _write_json(self,dic, fname = 'data.json'):
        """Функция получает словарь с данными и записывает его в файл"""
        with open(fname,'w',encoding="UTF-8") as fjs:
            json.dump(dic, fjs)   
            
    def _json_update(self, name: str, persid: str, level: str):
        """Функция получает данные и добавляет их в json файл"""
        # dic = json_read('data.json')
        if len(self.dic) > 0:
            for key, value in self.dic.items():
                if key == str(level):
                    value.setdefault(persid, name)
                    break
            else:
                self.dic.setdefault(level,{persid: name})
        else:
            self.dic.setdefault(level,{persid: name})
        # print(dic)
        return self.dic 
    
    def __str__(self):
        out = ""
        for string in self.users:
            out = out + str(string)+"\n" 
        return out
    
    def __repr__(self):
        out = ""
        for i in range(len(self.users)):
            # print(self.users[i].name,self.users[i].persid,self.users[i].level)
            out = out + f"Пользователь {self.users[i].name}, его id = {self.users[i].persid}, его уровень {self.users[i].level}\n"
        return out
    
    def _start_auth(self,dic) -> list:
        users = []
        if len(dic)>0:
            for key,value in dic.items():
                for key1, value1 in value.items():
                    users.append(User(value1,key1,key))
            # print(*(str(string)+"\n" for string in users))
        return users   
     
    def _check_dic(self,dic, persid):
        """"""
        if len(dic) > 0:
            for key, value in dic.items():
                for key1, value1 in value.items():
                    if key1 == persid:
                        return False
            else: 
                return True
        else:
            return True

    def _add_user(self) -> list:
        name_user = input("Введите ваше имя: ")
        uid_user = input("Введите ваш id: ")
        level_user = None
        for name,uid,level in self.log_in:
            if name == name_user and uid == uid_user:
                level_user = level  
        if level_user == '1':
            name = input("Введите имя пользователя: ")
            while True:
                persid = str(input("Введите идентификатор: "))
                if self._check_dic(self.dic, persid):
                    break 
            while True:
                level = int(input("Введите уровень доступа (1..7): "))
                if 0 < level < 8:
                    break      
            self.users.append(User(name,persid,level))  
            self._json_update(name, persid, level)
            self._write_json(self.dic)
            return self.users    
        else:
            raise LevelError(f"Пользователь {name_user} имеет {level_user} уровень. Для добавления новых пользователей уровень должнен быть =1")
        
    def print_users(self):
        print("Пользователь             id     level")
        for i in range(len(self.users)):
            print(f"{self.users[i].name:<20}    {self.users[i].persid:<5}   {self.users[i].level:<5}")

    def _log_in(self,name,uid,level):
        self.log_in.append([name,uid,level])
        return self.log_in    
            
    def check_access(self):
        name = input("Введите имя пользователя: ")
        uid = input("Введите id: ")
        temp_user = User(name,uid,"0")
        if temp_user in self.users:
            print("Пользователь есть в системе")
            for i in range(len(self.users)):
                # print(i, self.users[i].name,self.users[i].persid,self.users[i].level)
                if self.users[i].name == name:
                    return name,uid,self.users[i].level    
        else:
            raise AccessError("Пользователя нет в системе")
    
class User:
    def __init__(self,name,persid,level):
        self.name = name
        self.persid = persid
        self.level = level
        
    def __str__(self):
        return f"Пользователь {self.name}, его id = {self.persid}, его уровень {self.level}"
    
    def __repr__(self):
        return self
    
    def __eq__(self,other):
        return self.name == other.name and self.persid == other.persid
            
    
if __name__ == "__main__":
    users = Access()
    name,uid,level = users.check_access()
    users._log_in(name,uid,level)
    # log_in.append([name,uid,level])
    print(f"Пользователь найден. Его уровень = {level}. Список авторизованных пользователей {users.log_in}")
    
    users._add_user()
    print(f"Новый список пользователей: ")
    users.print_users()
    
