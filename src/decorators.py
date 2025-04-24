import functools
import logging
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования выполнения функций"""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Настройка логгера
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            # Очистка предыдущих обработчиков
            logger.handlers = []

            # Формат логов
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )

            # Выбор обработчика: файл или консоль
            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler()

            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                # Выполнение функции
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok. Result: {result}")
                return result
            except Exception as e:
                logger.error(
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                raise

        return wrapper

    return decorator


if __name__ == "__main__":
    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        """Сложение двух чисел."""
        return x + y

    @log()
    def div_function(a: float, b: float) -> float:
        """Деление двух чисел."""
        return a / b

    my_function(1, 2)
    try:
        div_function(1, 0)
    except ZeroDivisionError:
        pass
    