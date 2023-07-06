# 📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.


import datetime
import logging as log

FORMAT = "{levelname} - {asctime}: {msg}"
log.basicConfig(format = FORMAT, style="{", filename="info.log", level = log.INFO, encoding="utf-8", filemode='w')
logger = log.getLogger(__name__)

def parse_str(text: str):
    days = ["воскресеньe", "понедельник", "вторник", "среда", "четверг", "пятница", "суббота"]
    months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    day_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    week_day = 0
    month_day = 0
    num, day_week, month = text.split()
    try:
        int(num[0])
    except ValueError as e:
        log.info(f"Error. Неправильный формат запроса...") 
        exit(1)
    for i in range(len(days)):
        if days[i] == day_week:
            week_day = i
            break
    else:
        log.info(f"Error. Неправильный формат запроса...") 
        exit(1)
    for i in range(len(months)):
        if months[i] == month:
            month_day = i+1
            break
    else:
        log.info(f"Error. Неправильный формат запроса...") 
        exit(1)
    year= datetime.datetime.now().year
    count = 0
    for i in range(1,day_of_month[month_day-1]+1):
        day_str=f"{i}/{month_day}/{year}"
        date_object = datetime.datetime.strptime(day_str, '%d/%m/%Y')
        wk_day = date_object.strftime("%w")
        if int(wk_day) == week_day:
            count+=1
            if int(num[0]) == count:
                day = date_object.strftime("%d/%m/%Y")
                log.info(f"{num[0]}-й(ая) {days[week_day]} {months[month_day-1]} - это {day }")
                break
    else:
        log.info(f"Такого дня нету...")    
        
    
if __name__ == "__main__":
    parse_str("1-й четверг ноября")
    parse_str("2-я среда марта")
    parse_str("4-я пятница июня")
    parse_str("4-я вторник февраля")
    parse_str("5-я среда февраля")
    parse_str("-я среда февраля")
    parse_str("5-я февраля среда")