# 📌 Напишите для задачи 1 тесты pytest. Проверьте следующие
# варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

import pytest


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


def test_clear_str():
    assert clear_str("text") == 'text', 'возврат строки без изменений'


def test_case():
    assert clear_str("Text") == 'text', 'возврат строки с преобразованием регистра без потери'


def test_punctuation():
    assert clear_str("text: str") == 'text str', 'возврат строки с удалением знаков пунктуации'


def test_cyrillic():
    assert clear_str("text абрикос melon") == 'text  melon', 'возврат строки с удалением букв других алфавитов'


def test_all_changes():
    assert clear_str("Text, абрикос, melon.") == 'text  melon', 'возврат строки с учётом всех вышеперечисленных пунктов'


if __name__ == "__main__":
    pytest.main(["-v"])
