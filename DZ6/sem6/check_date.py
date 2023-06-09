# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ['check_date']


def check_date(text :str) -> bool:
    date = text.split('.')
    if 0 < len(date) <= 3:
        if (0 < int(date[0]) < 32) & (0 < int(date[1]) < 13) & (0 < int(date[2]) < 10000):
            if _check_vis(int(date[2])):
                if (int(date[1]) == 2) & (int(date[0]) < 30) | int(date[1]) != 2:
                    print(f"Дата {date[0]}.{date[1]}.{date[2]} верная")
                    print("Это високосный год\n")
                else:
                    print(f"Это неверная дата: {date[0]}.{date[1]}.{date[2]}, т.к. в феврале нет столько дней!\n")
            else:
                if (int(date[1]) == 2) & (int(date[0]) < 29) | int(date[1]) != 2:
                    print(f"Дата {date[0]}.{date[1]}.{date[2]} верная")
                    print("Это не високосный год\n")
                else:
                    print(f"Это неверная дата: {date[0]}.{date[1]}.{date[2]}, т.к. в феврале нет столько дней!\n")
        else:
            print(f"{text} - неправильная дата!!!\n")
    else:
        print(f"{text} - это вообще не похоже на дату!!!\n")        
            
            
def _check_vis(year: int =1900) -> bool:
    """Функция проверяет год на високосный"""
    CONST1 = 4
    CONST2 = 100
    CONST3 = 400
    
    if year % CONST1 == 0 & (year % CONST2 != 0 | year % CONST3 == 0):
        return True
    else:
        return False
        