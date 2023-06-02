# Пользователь вводит данные. Сделайте проверку данных 
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть 
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

def transform(text: str):
    if text.isdigit():
        if "." not in text:
            result = int(text)
            print("Целое")
    elif (text[0] == '-') & ('.' in text) & text.replace("-","").replace(".","").isdigit():
            result = float(text)
            print("Отрицательное вещественное")
    elif ('.' in text) & text.replace("-","").replace(".","").isdigit():
            result = float(text)        
            print("Вещественное")
    elif text.lower() != text:
            result = text.lower()
            print("Есть заглавные буквы, печатаем в нижнем регистре")
    else:
            result = text.capitalize()
            print("Нет заглавных букв, выводим первую заглавную")
    return result

print(transform("Text"))
print(transform("text"))
print(transform("-0kk.0"))
print(transform("1254"))
print(transform("25.25"))
print(transform("-25.25"))