# 📌 Создайте класс с базовым исключением и дочерние классы-
# исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class CustomException(Exception):
    pass

class LongError(CustomException):
    pass

class WidthError(CustomException):
    pass

class PositiveError(CustomException):
    pass
