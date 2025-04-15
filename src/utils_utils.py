import logging
from pathlib import Path

# Создаем логер для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования DEBUG

# Создаем file_handler для записи в файл
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)  # Создаем папку logs, если не существует
file_handler = logging.FileHandler(log_dir / "utils.log", mode="w", encoding="utf-8")

# Создаем форматтер
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Привязываем форматтер к handler
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)


def read_json_file(file_path: str) -> list[dict[str, any]]:
    """Читает JSON-файл и возвращает список словарей."""
    try:
        import json
        logger.debug(f"Попытка открыть файл: {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not isinstance(data, list):
                logger.error(f"Файл {file_path} содержит не список")
                return []
            logger.info(f"Успешно прочитан файл: {file_path}")
            return data
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {file_path}")
        return []
