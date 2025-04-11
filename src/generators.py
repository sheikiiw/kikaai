def filter_by_currency(transactions, currency_code):
    """Генератор, возвращающий транзакции в указанной валюте"""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор, возвращающий описания транзакций"""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, end):
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX"""
    for number in range(start, end + 1):
        # Форматируем число в строку с ведущими нулями до 16 символов
        card_num = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        formatted_card = f"{card_num[:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:]}"
        yield formatted_card
