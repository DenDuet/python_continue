# 📌 Создайте функцию, которая удаляет из текста все символы
# кроме букв латинского алфавита и пробелов.
# 📌 Возвращается строка в нижнем регистре.

def clear_str(text: str) -> str:
    """Функция получает строку, удаляет из текста все символы, кроме букв латинского алфавита и пробелов. И возвращает получившийся текст."""
    new_text = ""
    for char in text:
        if 'A' <= char <= 'z' or char == " ":
            new_text = new_text + char
    return new_text.lower()


if __name__ == "__main__":
    text = "At once, when я был маленьким, I whent outside home.?!"
    new_text = clear_str(text)
    print(text, "\n", new_text)
    