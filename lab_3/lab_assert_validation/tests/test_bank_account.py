import pytest
from src.bank_account import BankAccount


def test_initial_balance_default():
    account = BankAccount()
    assert account.get_balance() == 0


def test_initial_balance_custom():
    account = BankAccount(250)
    assert account.get_balance() == 250


def test_initial_balance_negative_raises_error():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount(-50)


def test_deposit_adds_money():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100


@pytest.mark.parametrize("invalid_amount", [0, -10])
def test_deposit_zero_or_negative_raises_error(invalid_amount):
    account = BankAccount()
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.deposit(invalid_amount)


def test_withdraw_removes_money():
    account = BankAccount(200)
    account.withdraw(50)
    assert account.get_balance() == 150


@pytest.mark.parametrize("invalid_amount", [0, -20])
def test_withdraw_zero_or_negative_raises_error(invalid_amount):
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.withdraw(invalid_amount)


def test_withdraw_exceeding_balance_raises_error():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(150)