# 📌 Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import unittest

class TestCaseName(unittest.TestCase):
    def test_method(self):
        self.assertEqual(clear_str("text"), 'text', msg='возврат строки без изменений')
    
    def test_case(self):
        self.assertEqual(clear_str("Text"), 'text', msg='возврат строки с преобразованием регистра без потери')
    
    def test_punctuation(self):
        self.assertEqual(clear_str("text: str"), 'text str', msg='возврат строки с удалением знаков пунктуации')
        
    def test_cyrillic(self):
        self.assertEqual(clear_str("text абрикос melon"), 'text  melon', msg='возврат строки с удалением букв других алфавитов')
        
    def test_all_changes(self):
        self.assertEqual(clear_str("Text, абрикос, melon."), 'text  melon', msg='возврат строки с учётом всех вышеперечисленных пунктов')        
    

def clear_str(text: str) -> str:
    """
    Функция получает строку, удаляет из текста все символы, кроме букв латинского алфавита и пробелов. И возвращает получившийся текст.
    >>> clear_str("text")
    'text'
    >>> clear_str("Text")
    'text'
    >>> clear_str("text: str")
    'text str'
    >>> clear_str("text абрикос melon")
    'text  melon'
    >>> clear_str("Text, абрикос, melon.")
    'text  melon'
    """
    new_text = ""
    for char in text:
        if 'A' <= char <= 'z' or char == " ":
            new_text = new_text + char
    return new_text.lower()


if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)
    unittest.main(verbosity=2)