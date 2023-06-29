# Создайте класс Моя Строка, где:
# - будут доступны все возможности str
# - дополнительно хранятся имя автора строки и время создания (time.time)
import time


class MyClass(str):
    """Класс расширяет стандартный класс работы со строками str."""
    def __new__(cls, value: str, name: str):
        """В этой функции создается новый экземпляр класса MyString."""
        instance = super().__new__(cls,value)
        instance.name = name
        instance.created_at = time.time()
        return instance
    
    
if __name__ == '__main__':
    mystr = MyClass('Cтрока', 'параметр')
    print(mystr.created_at)
    print(mystr.name)
    print(mystr)
    print(mystr.upper())
    help(MyClass)
        
    