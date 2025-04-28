import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/masks.log', mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.ERROR)


def get_mask_card_number(card_number: str):
    """возвращает замаскированный номер карты"""
    logger.info(f"Вызвана get_mask_card_number с аргументом: {card_number}")
    card_number_str = str(card_number)
    result = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    logger.info(f"Результат: {result}")
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: str):
    """возвращает замаскированный номер банковского счета"""
    logger.info(f"Вызвана get_mask_account с аргументом: {account_number}")
    account_number_str = str(account_number)
    result = f"**{account_number_str[-4:]}"
    logger.info(f"Результат: {result}")
    return result
