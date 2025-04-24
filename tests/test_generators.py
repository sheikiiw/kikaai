import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}, "amount": "100"},
            "description": "Test USD 1"
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB"}, "amount": "200"},
            "description": "Test RUB"
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}, "amount": "300"},
            "description": "Test USD 2"
        }
    ]


def test_filter_by_currency_usd(sample_transactions):
    usd_trans = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_trans) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in usd_trans)


def test_filter_by_currency_empty_result(sample_transactions):
    eur_trans = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_trans) == 0


def test_filter_by_currency_empty_list():
    empty_trans = list(filter_by_currency([], "USD"))
    assert len(empty_trans) == 0


def test_transaction_descriptions(sample_transactions):
    desc = list(transaction_descriptions(sample_transactions))
    assert desc == ["Test USD 1", "Test RUB", "Test USD 2"]


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


@pytest.mark.parametrize("start,end,expected_count", [
    (1, 3, 3),
    (5, 5, 1),
    (10, 12, 3),
])


def test_card_number_generator_count(start, end, expected_count):
    cards = list(card_number_generator(start, end))
    assert len(cards) == expected_count


def test_card_number_generator_format():
    cards = list(card_number_generator(1, 2))
    assert cards[0] == "0000 0000 0000 0001"
    assert cards[1] == "0000 0000 0000 0002"


def test_card_number_generator_edge_cases():
    cards = list(card_number_generator(9999_9999_9999_9998, 9999_9999_9999_9999))
    assert cards[0] == "9999 9999 9999 9998"
    assert cards[1] == "9999 9999 9999 9999"