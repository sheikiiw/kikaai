from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account: str):
    """Функция маскировки"""
    name = account.split()
    number = name.pop()
    if "Счет" in account:
        return f"Счет {get_mask_account(number)}"
    else:
        return " ".join(name) + " " + get_mask_card_number(number)


def get_date(date: str):
    """Вывод даты"""
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    uni = f"{day}.{month}.{year}"
    return uni
