# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = ['Коля',["рюкзак", "спальник", "ручка", "кружка", "миска", "ложка"],'Саша',["рюкзак", "кружка", "спальник", "ложка"], 'Женя',[ "ручка","рюкзак", "кружка", "ложка"]]
dict = {}

hike.append('Толя')
hike.append(["рюкзак", "ручка", "кружка", "ложка", "телефон","спальник"])
   
for i in range(0,len(hike),2):
    dict.setdefault(hike[i], set(hike[i+1]))

l_keys = list(dict)
equipment = []

for i in l_keys:
    equipment.append(dict[i])

for i in range(len(l_keys)):
    print(f"Друзья взяли такие вещи: {l_keys[i]} - {equipment[i]}")

setUnique = set()
for i in equipment:
    setUnique = setUnique.union(set(i))
print(f"\nОбщий список вещей: {setUnique}\n")

setAll = set(equipment[0])

for i in range(1,len(l_keys)):
    setAll = setAll & equipment[i]

print(f"Все друзья взяли такие вещи (вещи есть у всех): {setAll}\n")

for i in range(len(l_keys)):
    print(f"Уникальные вещи у {l_keys[i]} -> {equipment[i]-setAll}")

for i in setUnique:
    count = 0
    friend = 0
    for j in range(len(l_keys)):
        if i in equipment[j]:
            count += 1
            friend = j
    if count == 1:
        print(f"\nУ {l_keys[friend]} уникальный предмет: {i}")


