import pytest


@pytest.fixture
def operation_data_with_from() -> dict:
    return {
        "id": 649467725,
        "state": "EXECUTED",
        "date": "2018-04-14T19:35:28.978265",
        "operationAmount": {
            "amount": "96995.73",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 2256483756542539",
        "to": "Счет 97584898735659638967"
    }


@pytest.fixture
def operation_data_without_from(operation_data_with_from):
    operation_data_with_from['description'] = 'Открытие вклада'
    del operation_data_with_from['from']
    return operation_data_with_from
