# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

# *Верните все возможные варианты комплектации рюкзака.

things = {"палатка": 5, "Топор": 3, "Миска": 1,  "Кружка": 1, "Вода": 4, "печка": 5, "спальник": 3, "одежда": 5, "обувь": 5, "еда": 10, "компас": 1}

MAX_WEIGHT = 25 # грузоподъемность рюкзака
print(f"Список предметов для похода: {things}. Грузоподьемность рюкзака: {MAX_WEIGHT}\n")
data_items = things.items()
backpack = []
weight = 0
for key,value in data_items:
    weight = weight + value
if weight-MAX_WEIGHT > 0:
    print(f"Общий вес предметов: {weight}. Перевес = {weight-MAX_WEIGHT}.\n")
    things_list = list(data_items)
    for i in range(len(things_list)):
        backpack = []
        weight = 0
        for key,value in things_list:
            if weight + value <= MAX_WEIGHT:
                backpack.append(key)
                weight = weight + value
        print(f"{i+1:>2}. Такой список вещей получился в рюкзаке {backpack} и на такой вес: {weight}")
        things_list = things_list[1:]+things_list[:1]
else:
    print(f"Общий вес предметов: {weight}. Все предметы влезут в рюкзак.")



