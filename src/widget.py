def get_mask_card_number(number: str):
    """Срез чисел"""
    delive = number[:13]
    zeebbed = number[14:18]
    fancy = number[18:20]
    many = number[-4:]

    return f"{delive} {zeebbed} {fancy} **** {many}"


def get_mask_account(number: str):
    """Возврат замаскированного числа"""
    meow = number[-4:]
    return f"{meow}"



def get_date(date: str):
    """Вывод даты"""
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    uni = f"{day}.{month}.{year}"
    return uni
