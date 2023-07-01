# 📌 Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

from random import randint

class Chess:
    def __init__(self):
        self.queen = self.rand_queen() 
        
    def chess(self,queen):
        """Функция проверяет список с координатами ферзей (queen) на пересечение, если оно есть, 
        то возвращается False иначе True"""
        for i in range(0,8):
            for j in range(i+1,8):
                if queen[i][0] == queen[j][0]:
                    return False
                elif queen[i][1] == queen[j][1]:
                    return False
                elif abs(queen[i][0] - queen[j][0]) == abs(queen[i][1] - queen[j][1]):
                    return False
        else:
            return True
        
    def rand_queen(self):
        """Функция генерирует список с координатами расстановки ферзей, отправляет в функцию
        chess на проверку, правильные комбинации распечатывает."""
        _COUNT = 4
        count = _COUNT
        queen_count = []
        while count > 0:
            queen = []
            for i in range(1,9):
                queen.append([i,randint(1,8)])
            res = self.chess(queen)
            if res:
                print(f"{_COUNT-count+1}. Положение ферзей с такими координатами: \n{queen} \nбезопасно для них.\n")
                count-=1
                queen_count.append(queen)            
        return queen_count

if __name__ == "__main__":
    queen = Chess()