from typing import Callable, Optional, Any
import functools

from pyexpat.errors import messages


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функции.
    Логирует успешное выполнение функции или возникшие исключения.
    Логи можно выводить в консоль (по умолчанию) или записывать в файл.
    """

    def decorator(func: Callable) -> Callable:
        """
        Принимает функцию, которую надо обернуть,
        возвращает обернутую функцию с логированием.
        """
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обертка, которая собственно выполняет функцию
            и логирует результат или ошибку
            """
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                    raise

        return wrapper

    return decorator


@log(filename="log.txt")
def my_function(x, y):
    return x + y


if __name__ == "__main__":
    print(my_function(1, 2))
