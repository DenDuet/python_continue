# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-
# архивов
# 📌 list-архивы также являются свойствами экземпляра


class Archive:
    """Это класс Архив."""
    numbers = []
    values = []
    
    def __new__(cls, number: int, value: str):
        """Это функция создает новый экземпляр класса."""
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance
    
    def __init__(self, number: int, value: str):
        """Это функция инициализирует созданный экземпляр класса."""
        self.number = number
        self.value = value
        
    def __repr__(self):
        return f"Archive({self.number}, '{self.value}')"
    
    def __str__(self):
        return f'Номер: {self.number}, Значение: {self.value}'
    
        
if __name__ == '__main__':
    a1 = Archive(1, 'Один')
    print(f'{a1.numbers}, {a1.values}')
    a2 = Archive(2, 'Два')
    print(f'{a1.numbers= }, {a1.values= }')
    a3 = Archive(3, 'Три')
    print(f'{a2=}')
    print(a1)
    help(Archive)