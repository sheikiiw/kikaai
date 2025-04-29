from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_string: str) -> str:
    """Функция маскировки счета и карт"""
    number_list = number_string.split()
    number = number_list.pop()
    name_card = " ".join(number_list)
    if "Счет" in name_card:
        return f"Счет {get_mask_account(number)}"
    else:
        return f"{name_card} {get_mask_card_number(number)}"

def get_date(date: str):
    """Форматирует дату в вид ДД.ММ.ГГГГ."""
    if not date or len(date) != 10 or date[4] != '-' or date[7] != '-':
        raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    res = f"{day}.{month}.{year}"
    return res
