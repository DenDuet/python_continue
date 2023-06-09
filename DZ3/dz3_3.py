# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

things = {"палатка": 5, "печка": 5, "спальник": 3, "одежда": 5, "обувь": 5, "еда": 10, "компас": 1}

MAX_WEIGHT = 32 # грузоподъемность рюкзака

data_items = things.items()
backpack = []
weight = 0
for key,value in data_items:
    if weight + value <= MAX_WEIGHT:
        backpack.append(key)
        weight = weight + value

print(f"Такой список вещей получился в рюкзаке {backpack} и на такой вес: {weight}")

