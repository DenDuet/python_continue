# 📌 Создайте функцию аналог get для словаря.
# 📌 Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# 📌 При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# 📌 Реализуйте работу через обработку исключений.


def get(dic: dict, key: str):
    value_def: str="нет_в_словаре "
    try:
        value = dic[key]
        print(f"Ключ {key} есть в словаре. Его значение = {value}")
        return value
    except KeyError as e:
        print(f"Такого ключа ({key}) нет в словаре. Возвращаем дефолтное значение {value_def}")
        return value_def
    
if __name__ == "__main__":
    dic = {"1":"один","2":"два","3":"три"}
    print(f"Словарь: {dic}")
    key = "2"
    print(f"Ищем по ключу {key} получаем значение: {get(dic,key)}")
    key = "5"
    print(f"Ищем по ключу {key} получаем значение: {get(dic,key)}")