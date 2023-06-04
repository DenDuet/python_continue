# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

N = 100


def simple_number(number):
    """Генератор последовательно выдает простое число от 2 до numbers."""
    for i in range(2,number):
        simple=True
        for j in range(2,i):
            if i%j == 0:
                simple = False
                break
        if simple:
            yield i


print(*(simple_number(N)))