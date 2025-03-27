def get_mask_card_number(number: str):
    delive = number[:13]
    zeebbed = number[14:18]
    fancy = number[18:20]
    many = number[-4:]
    """Срез чисел"""
    return f"{delive} {zeebbed} {fancy} **** {many}"


def get_mask_account(number: str):
    meow = number[-4:]
    return f"{meow}"
    """Возврат замаскированного числа"""


def get_date(date: str):
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    uni = f"{day}.{month}.{year}"
    return uni
   """Вывод даты"""