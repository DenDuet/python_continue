# ✔ Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.


list1 = [1, 2, 4, 2, 1, 5, 7, 4]

def unique(num: list) -> list:
    result = []
    for i in num:
        if list1.count(i) > 1:
            result.append(i)
    return set(result)


print(f"Список изначальный {list1}\nсписок уникальный - {unique(list1)}")
