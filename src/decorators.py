import time
from functools import wraps


def log(filename):
    """Декоратор, который автоматически регистрирует детали выполнения функций,
    такие как время вызова, имя функции, передаваемые аргументы, результат выполнения и
    информация об ошибках"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            message = ""
            result = None

            try:
                start_time = time.time()
                result = func(*args, **kwargs)
                log_message = f"Функция: {func.__name__}\nРезультат: {
                              result}\nВремя выполнения: {time.time() - start_time}\n"
                message = log_message
            except Exception as e:
                error_message = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"
                message = error_message

            if filename:
                with open(filename, "a", encoding="utf-8") as log_file:
                    log_file.write(message)
            else:
                print(message)
            return result

        return inner

    return wrapper


@log("mylog.txt")
def func(x, y):
    if x < 0 and y < 0:
        raise ValueError("Отрицательное число")
    return x + y
