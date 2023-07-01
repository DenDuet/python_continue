# 📌 Создайте класс с базовым исключением и дочерние классы-
# исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class CustomException(Exception):
    pass

class LevelError(CustomException):
    pass

class AccessError(CustomException):
    pass
