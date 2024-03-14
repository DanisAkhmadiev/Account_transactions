import pytest
from code.main import (executed_operations, convert_date, print_last_5_operations, mask_card_number, get_card_name)


def test_executed_operations():
    operations = [
        {"state": "EXECUTED"},
        {"state": "CANCELED"},
        {"state": "CANCELED"},
        {"state": "EXECUTED"}
]
    assert executed_operations(operations) == [{"state": "EXECUTED"}, {"state": "EXECUTED"}]


def test_convert_date():
    operation = {"date": "2022-01-05T08:30:00.000000"}
    assert convert_date([operation])[0]["date"] == "05.01.2022"


def test_print_last_5_operations():
    operations = [{"date": "2022-01-01"}, {"date": "2022-01-02"}, {"date": "2022-01-03"}]
    assert print_last_5_operations(operations) == [{"date": "2022-01-03"}, {"date": "2022-01-02"}, {"date": "2022-01-01"}]


def test_mask_card_number():
    assert mask_card_number("Card 1234 5678 9012 3456") == "1234 56** **** 3456"

#
def test_get_card_name():
    assert get_card_name("Card 1234 5678 9012 3456") == "Card"



if __name__ == "__main__":
    pytest.main()


