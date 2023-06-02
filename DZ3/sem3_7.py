# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.

# text = input("Введите строку: ")
text = "hdh hkhkhl yiuyi kjjkh кенкк выфв uiu ew"
dict = {}

for i in range(len(text)):
    char = text[i]
    char_count = 1
    for j in range(i+1,len(text)):
        if text[j] == char:
            char_count+=1
    dict.setdefault(char,char_count)
    print(f"Словарь: Буква {char} встречается {dict.setdefault(char)}, Буква {char} встречается {text.count(char)} раз")
print(dict)