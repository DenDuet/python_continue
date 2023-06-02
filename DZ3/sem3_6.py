# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного 
# слова был один пробел между ним и номером строки.

# text = input("Введите строку: ")
text = "hdh hkhkhl yiuyi kjjkh кенкк выфв uiu ew"
textarr = text.split()
textarr.sort()
print(textarr)

max = 0
for i in textarr:
    if len(i) > max:
        max = len(i)
print(max)

for i in range(1,len(textarr)):
    print(f"{i:>2}. {textarr[i]:>{max}}")
