def get_mask_card_number(number: str):
    """Маскирует номер карты, скрывая часть цифр"""
    if not number or len(number) < 20:
        raise ValueError("Номер карты должен содержать минимум 20 символов")
    first = number[:13]
    second = number[14:18]
    third = number[18:20]
    last = number[-4:]
    return f"{first} {second} {third} **** {last}"


def get_mask_account(number: str):
    """Возвращает замаскированный номер счета"""
    if not number or len(number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 символа")
    once = number[-4:]
    return f"**** {once}"  # Добавляем маскировку для большей наглядности


def get_date(date: str):
    """Форматирует дату в вид ДД.ММ.ГГГГ."""
    if not date or len(date) != 10 or date[4] != '-' or date[7] != '-':
        raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    res = f"{day}.{month}.{year}"
    return res
