# ✔ Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT = 10

count = COUNT
num = randint(LOWER_LIMIT, UPPER_LIMIT)

while count > 0:
    number = int(input(f"Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: "))
    if number == num:
        print(f"Вы угадали число за {COUNT-count} попыток.")
        break
    elif number > num:
        print(f"Загаданное число меньше, чем {number} ")
    elif number < num:
        print(f"Загаданное число больше, чем {number} ")
        
    count-=1
    print(f"Осталось {count} попыток")
else:
    print(f"Вы не угадали число за {COUNT} попыток.")
    

