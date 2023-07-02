# 📌 Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# 📌 возврат строки без изменений
# 📌 возврат строки с преобразованием регистра без потери
# символов
# 📌 возврат строки с удалением знаков пунктуации
# 📌 возврат строки с удалением букв других алфавитов
# 📌 возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)


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
    import doctest
    doctest.testmod(verbose=True)
    # text = "At once, when я был маленьким, I whent outside home.?!"
    # new_text = clear_str(text)
    # print(text, "\n", new_text)
