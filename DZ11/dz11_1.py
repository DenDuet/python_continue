# 📌 Решить задачи, которые не успели решить на семинаре.
# 📌 Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.
# 📌 Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

class Matrix:
    """Класс выводит матрицу на печать, также сравнивает 2 матрицы, складывает и умножает их."""
    matr = [[],]
    def __init__(self,matr: list):
        """Функция инициализирует новую матрицу."""
        self.matr = matr
        
    def __eq__(self, other):
        """Функция сравнивает матрицы и выводит заключение об их равенстве."""
        if len(self.matr) == len(other.matr):
            if len(self.matr[0]) == len(other.matr[0]):
                for i in range(len(self.matr)):
                    for j in range(len(self.matr[0])):
                        if self.matr[i][j]!=other.matr[i][j]:
                            return "Матрицы не равны."
        return "Матрицы равны."
    
    def __mul__(self, other):
        l1 = l2 = 0
        if (len(self.matr) == len(other.matr[0])):
            l1 = len(self.matr)
            l2 = len(other.matr[0])
        if (len(self.matr[0]) == len(other.matr)):
            l1 = len(self.matr[0])
            l2 = len(other.matr)
        if l1!=0 and l2!=0:
            new_matr = []
            new_matr_str = 0
            for i in range(l1):
                for j in range(l2):
                    new_matr_str = new_matr_str + (self.matr[i][j] * other.matr[j][i])
                new_matr.append(new_matr_str)
                new_matr_str = 0
        return Matrix(new_matr)  
        
        
    def __add__(self, other):
        """Функция суммирует элементы матриц."""
        new_matr = []
        new_matr_str = []
        for i in range(len(self.matr)):
            for j in range(len(self.matr[i])):
                new_matr_str.append(self.matr[i][j] + other.matr[i][j])
            new_matr.append(new_matr_str)
            new_matr_str = []
        return Matrix(new_matr)  

    def __str__(self):
        print("\nМатрица:")
        for i in range(len(self.matr)):
            print(self.matr[i])
        return f"Матрица: {self.matr}"
    
if __name__ == "__main__":
    matr = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = Matrix(matr)
    print(matrix)  
    matr1 = [[2,2,2],[3,3,3],[4,5,6]]
    matrix1 = Matrix(matr1)
    print(matrix1)   
    matri = matrix + matrix1
    print("Матрица суммы: ", matri)

    matri = matrix * matrix1
    print("Матрица произведения: ", matri)
    
    print(f'Сравнение матриц: {matrix == matrix = }')
    print(f'Сравнение матриц: {matrix == matrix1 = }')
    help(Matrix)