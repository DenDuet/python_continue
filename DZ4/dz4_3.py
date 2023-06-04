# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.


START_SUM = 0
OPERAT_SUM = 50
PROC_SUM = 1.5
COMIS_SUM_MIN = 30
COMIS_SUM_MAX = 600
BONUS = 3
PROC_SUM_3 = 3
MAX_SUM = 5000000
MAX_SUM_TAX = 10

number_operate = BONUS
sum = START_SUM

withdrawal = []
replenishment = []


def inp(text) -> int | float:
    """Функция запрашивает данные у пользователя, выводя ему сообщение."""
    return input(text)


def decrease(sum, operation) -> int | float:
    """Функция уменьшает сумму на величину снятия (operation) и записывает сумму в список withdrawal"""
    sum = sum - operation
    if sum < 0:
        print(f"На счету образовался отрицательный остаток: {round(sum,2)}! Необходимо пополнить счет!")
    withdrawal.append(operation)
    return round(sum,2)
    

def increase(sum, operation) -> int | float:
    """Функция увеличивает сумму на величину снятия (operation) и записывает сумму в список replenishment"""
    sum = sum + operation
    replenishment.append(operation)
    return sum
 
    
def print_increase():
    """Функция печатает список пополнения."""
    print(f"\nСписок пополнения счета: {replenishment}\n")
    

def print_decrease():
    """Функция печатает список снятия."""
    print(f"\nСписок уменьшения счета: {withdrawal}\n")

    
while True:
    print(f"\nНа вашем счету: {sum} у.е.")
    command = inp(f"\nВыберите действие: \n1 - пополнить, \n2 - снять,  \n3 - распечатать список пополнения,\n4 - распечатать список снятия,\n5 - выйти\n: ")
    match command:
        case "1":
            k = int(inp(f"Введите сумму пополнения кратно {OPERAT_SUM} у.е.: "))
            if k//OPERAT_SUM > 0:
                operation = (k//OPERAT_SUM)*OPERAT_SUM
                sum = increase(sum, operation)
                number_operate-=1
                
        case "2":
            k = int(inp(f"Введите сумму снятия кратно {OPERAT_SUM} у.е.: "))
            if k >= sum: 
                print("На счету недостаточно денег...")
            elif k//OPERAT_SUM > 0:
                operation = (k//OPERAT_SUM)*OPERAT_SUM
                sum = decrease(sum, operation)
                number_operate-=1
                if k * PROC_SUM/100 < COMIS_SUM_MIN:
                    operation = COMIS_SUM_MIN
                elif k * PROC_SUM/100 > COMIS_SUM_MAX:
                    operation = COMIS_SUM_MAX
                else:
                    operation = round(k * PROC_SUM/100,2)
                sum = decrease(sum, operation)

        case "3":
            print_increase()
            
        case "4":
            print_decrease()       
         
        case "5":
            exit(0)
        case _:
            exit(0)
    if number_operate==0:
        sum = increase(sum, round(sum * PROC_SUM_3/100,2))
        number_operate = BONUS    
    if sum > MAX_SUM:
        sum = decrease(sum, round(sum * MAX_SUM_TAX/100,2))