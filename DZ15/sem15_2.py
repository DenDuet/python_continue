# 📌 На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# 📌 Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

from typing import Callable
import logging as log

log.basicConfig(filename="debug.log", level = log.DEBUG, encoding="utf-8", filemode='w')
logger = log.getLogger(__name__)


def  decor_log(func: Callable):
    dic = {} 
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        dic.update({res: args})
        dic.update({**kwargs})
        log.debug(f'{dic}')
        dic.update()
    return wrapper
        
@decor_log
def func_sum(number: int, number2: int, *args, **kwargs) -> int:
    return number + number2


if __name__ == "__main__":
    f= func_sum(18,110,a=6,b=8)
    f= func_sum(4,5,c=2,d=4)
    f= func_sum(18,10,w=12,f=5)
