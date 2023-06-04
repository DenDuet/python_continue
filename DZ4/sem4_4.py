# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.


def sort_list(numbers,way="down") -> list:
    """Функция сортирует список чисел"""
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if way == "up":
                if numbers[j] > numbers[j+1]:
                    tmp = numbers[j]
                    numbers[j] = numbers[j+1]
                    numbers[j+1] = tmp
            else:
                if numbers[j] < numbers[j+1]:
                    tmp = numbers[j+1]
                    numbers[j+1] = numbers[j]
                    numbers[j] = tmp
    return numbers


list_num = [1, 3, 5, 11, 2, 0, 4, 44, 21, 12, 11]
print(f"Массив чисел: {list_num}")
list_num_sort = sort_list(list_num)
print(f"Массив чисел, отсортированный по убыванию значений: {list_num}")
list_num_sort = sort_list(list_num, "up")
print(f"Массив чисел, отсортированный по возрастанию значений: {list_num}")
        
