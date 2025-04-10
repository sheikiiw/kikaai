def get_mask_card_number(number: str) -> str:
    """Маскирует номер карты, оставляя видимыми определенные части."""
    delive = number[:13]
    zeebbed = number[14:18]
    fancy = number[18:20]
    many = number[-4:]
    return f"{delive} {zeebbed} {fancy} **** {many}"


def get_mask_account(number: str) -> str:
    """Возвращает замаскированный номер счета, показывая последние 4 цифры."""
    meow = number[-4:]
    return f"{meow}"


def get_date(date: str) -> str:
    """Преобразует дату в формат ДД.ММ.ГГГГ."""
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    uni = f"{day}.{month}.{year}"
    return uni
