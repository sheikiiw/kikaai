def filter_by_state(transactions, state='EXECUTED'):
    """фильтрует список транзакций по состоянию"""
    return [transaction for transaction in transactions if transaction.get('state') == state]

def sort_by_date(transactions, reverse=True):
    """сортирует список транзакций по дате"""
    return sorted(transactions, key=lambda x: x['date'], reverse=reverse)