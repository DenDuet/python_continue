# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.


def sum_num(numbers, min, max) -> int:
    """Функция считает сумму элементов списка от min до max (или до конца списка)"""
    if min < 0:
        min = 0
    if max >= len(numbers):
        max = len(numbers)-1
    sum_num = 0
    
    for i in range(min,max+1):
        sum_num = sum_num + numbers[i]
    return sum_num


NUM1 = 3
NUM2 = 6
nums = [100, 2, 4, 81, 17, 21, 4]
print(f"Сумма элементов списка {nums} от {NUM1} до {NUM2} = {sum_num(nums,NUM1,NUM2)}")
