from datetime import datetime
from src.dto import Payment, Operation


def test_init_payment_from_str():
    payment = Payment.init_from_str('Visa Classic 6831982476737658')
    assert payment.name == 'Visa Classic'
    assert payment.number == '6831982476737658'


def test_safe_payment_for_amount():
    payment = Payment(name='Счет', number='64686473678894779589')
    assert payment.safe() == 'Счет **9589'


def test_safe_payment_for_card_number():
    payment = Payment(name='MasterCard', number='3152479541115065')
    assert payment.safe() == 'MasterCard 3152 47** **** 5065'


def test_split_card_number_by_blocks():
    card_number = '1596837868705199'
    result = Payment.split_card_number_by_blocks(card_number)
    assert result == '1596 8378 6870 5199'


def test_init_operation_from_dict(operation_data_without_from):
    op = Operation.init_from_dict(operation_data_without_from)

    assert op.id == 649467725
    assert op.state == "EXECUTED"
    assert op.date == datetime(2018, 4, 14, 19, 35, 28, 978265)
    assert op.amount.value == 96995.73
    assert op.amount.currency_name == 'руб.'
    assert op.amount.currency_code == 'RUB'
    assert op.description == "Открытие вклада"
    assert op.payment_to.name == 'Счет'
    assert op.payment_to.number == '97584898735659638967'
    assert op.payment_from is None


def test_safe_operation_with_from(operation_data_with_from):
    operation = Operation.init_from_dict(operation_data_with_from)
    expected_result = (
        '14.04.2018 Перевод организации\n'
        'Visa Platinum 2256 48** **** 2539 -> Счет **8967\n'
        '96995.73 руб.'
    )
    assert operation.safe() == expected_result


def test_safe_operation_without_from(operation_data_without_from):
    operation = Operation.init_from_dict(operation_data_without_from)
    expected_result = (
        '14.04.2018 Открытие вклада\n'
        'Счет **8967\n'
        '96995.73 руб.'
    )
    assert operation.safe() == expected_result
