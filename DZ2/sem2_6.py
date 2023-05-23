# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

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

while True:
    print(f"\nНа вашем счету: {sum} у.е.")
    command = input(f"\nВыберите действие: \n1 - пополнить, \n2 - снять, \n3 - выйти\n: ")
    match command:
        case "1":
            k = int(input(f"Введите сумму пополнения кратно {OPERAT_SUM} у.е.: "))
            if k//OPERAT_SUM > 0:
                sum = sum + (k//OPERAT_SUM)*OPERAT_SUM
                number_operate-=1
        case "2":
            k = int(input(f"Введите сумму снятия кратно {OPERAT_SUM} у.е.: "))
            if k >= sum: 
                print("На счету недостаточно денег...")
            elif k//OPERAT_SUM > 0:
                sum = sum - (k//OPERAT_SUM)*OPERAT_SUM
                number_operate-=1
                if k * PROC_SUM/100 < COMIS_SUM_MIN:
                    sum = sum - COMIS_SUM_MIN
                elif k * PROC_SUM/100 > COMIS_SUM_MAX:
                    sum = sum - COMIS_SUM_MAX
                else:
                    sum = sum - round(k * PROC_SUM/100,2)
        case "3":
            exit(0)
        case _:
            exit(0)
    if number_operate==0:
        sum = sum + round(sum * PROC_SUM_3/100,2)        
        number_operate = BONUS    
    if sum > MAX_SUM:
        sum = sum - round(sum * MAX_SUM_TAX/100,2)
                
            
            
                