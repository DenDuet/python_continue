# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).

N = 40


def fib(N):
    """Генератор чисел Фибоначчи."""
    fib = [0,1,]
    for i in range(0, N):
        if i>= 2:
            fib.append(fib[i-2]+fib[i-1])
        yield fib[i]


fib_num = fib(N)

for i in fib_num:
    print(i, end=' ')