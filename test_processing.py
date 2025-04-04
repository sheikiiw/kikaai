import pytest
from processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {"state": "EXECUTED", "date": "2023-10-01"},
        {"state": "PENDING", "date": "2023-10-02"},
        {"state": "EXECUTED", "date": "2023-10-03"},
    ]

def test_filter_by_state(sample_data):
    assert filter_by_state(sample_data) == [
        {"state": "EXECUTED", "date": "2023-10-01"},
        {"state": "EXECUTED", "date": "2023-10-03"},
    ]
    assert filter_by_state(sample_data, "PENDING") == [
        {"state": "PENDING", "date": "2023-10-02"},
    ]
    assert filter_by_state(sample_data, "NON_EXISTENT") == []

def test_sort_by_date(sample_data):
    sorted_data = sort_by_date(sample_data, descending=True)
    assert sorted_data[0]["date"] == "2023-10-03"
    assert sorted_data[1]["date"] == "2023-10-02"
    assert sorted_data[2]["date"] == "2023-10-01"

    sorted_data_asc = sort_by_date(sample_data, descending=False)
    assert sorted_data_asc[0]["date"] == "2023-10-01"
    assert sorted_data_asc[1]["date"] == "2023-10-02"
    assert sorted_data_asc[2]["date"] == "2023-10-03"