# Напишите функцию для транспонирования матрицы


def transp(matr) -> list:
    """Функция транспонирует исходную матрицу и возвращает транспонированную"""
    row = len(matr)
    col = len(matr[0])
    new_matr = [[0] * row for i in range(col)]  
    print_matr(matr, "Исходная матрица")

    for i in range(row):
        for j in range(col):
            new_matr[j][i] = matr[i][j]

    return new_matr


def print_matr(matr,text):
    """Функция выводит на экран матрицу"""
    row = len(matr)
    col = len(matr[0])
    print(f"\n{text}\n")
    for i in range(row):
        for j in range(col):
            print(matr[i][j],end='')
        print()    
    

matr = [[1,2,3,4],[4,5,6,7],[7,8,9,0]]
# matr = [[1,3,4],[4,5,6],[8,9,0]]
new_matr = transp(matr)
print_matr(new_matr, "Транспонированная матрица")