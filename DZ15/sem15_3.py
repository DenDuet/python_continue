# 📌 Доработаем задачу 2.
# 📌 Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import datetime
from typing import Callable
import logging as log

FORMAT = "{levelname} - {asctime}: {msg}"
log.basicConfig(format = FORMAT, style="{", filename="info.log", level = log.INFO, encoding="utf-8", filemode='w')
logger = log.getLogger(__name__)


def  decor_log(func: Callable):
    dic = {} 
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        dic.update({res: args})
        a, b = args
        dic.update({**kwargs})
        log.info(f'{func.__name__}, {dic}, {a} + {b} = {a+b}')
        dic.update()
    return wrapper
        
@decor_log
def func_sum(number: int, number2: int, *args, **kwargs) -> int:
    return number + number2


if __name__ == "__main__":
    f= func_sum(18,110,a=6,b=8)
    f= func_sum(4,5,c=2,d=4)
    f= func_sum(18,10,w=12,f=5)