import logging
from pathlib import Path

# Создаем логер для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования DEBUG

# Создаем file_handler для записи в файл
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)  # Создаем папку logs, если не существует
file_handler = logging.FileHandler(log_dir / "masks.log", mode="w", encoding="utf-8")

# Создаем форматтер
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Привязываем форматтер к handler
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
logger.addHandler(file_handler)


def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры."""
    logger.debug(f"Попытка маскировки номера карты: {card_number}")
    if not card_number.isdigit() or len(card_number) != 16:
        logger.error(f"Некорректный номер карты: {card_number}")
        return "Некорректный номер"
    masked = f"{card_number[:6]}******{card_number[-4:]}"
    logger.info(f"Успешно замаскирован номер карты: {masked}")
    return masked
