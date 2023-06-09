# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


from sys import argv
import sem6.check_date as cal


if __name__ == '__main__':
    if (len(argv) > 1):
        res = cal.check_date(argv[1])    
    else:
        print("Нужно передать аргумент: дата в формате DD.MM.YYYY")
        print("Пример: python check_date_commandline.py 01.12.2000")
        # cal.check_date("01.12.2000")