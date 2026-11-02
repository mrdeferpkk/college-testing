import pytest
from src.main import BankAccount

# 1. Тести ініціалізації та успішного отримання балансу
def test_create_account():
    account = BankAccount("Іван", 500.0)
    assert account.owner == "Іван"
    assert account.get_balance() == 500.0

# 2. Тест поповнення рахунку
def test_deposit(default_account):
    default_account.deposit(250.5)
    assert default_account.get_balance() == pytest.approx(1250.5)

# 3. Тест зняття коштів
def test_withdraw(default_account):
    default_account.withdraw(300.0)
    assert default_account.get_balance() == 700.0

# 4. Тест нарахування відсотків
def test_add_interest(default_account):
    default_account.add_interest(10.0)  # 10% від 1000 = 100
    assert default_account.get_balance() == pytest.approx(1100.0)

# 5. Параметризовані тести для перевірки помилок ініціалізації (TypeError / ValueError)
@pytest.mark.parametrize(
    "owner, balance, expected_exception, error_message",
    [
        (123, 100.0, TypeError, "Owner must be a string"),
        ("", 100.0, ValueError, "Owner name cannot be empty"),
        ("Петро", "invalid", TypeError, "Balance must be a number"),
        ("Петро", -50.0, ValueError, "Initial balance cannot be negative"),
    ],
)
def test_account_init_exceptions(owner, balance, expected_exception, error_message):
    with pytest.raises(expected_exception) as exc_info:
        BankAccount(owner, balance)
    assert error_message in str(exc_info.value)

# 6. Тести винятків при некоректному поповненні та знятті
def test_deposit_exceptions(default_account):
    with pytest.raises(TypeError):
        default_account.deposit("100")
    with pytest.raises(ValueError):
        default_account.deposit(-50)
    with pytest.raises(ValueError):
        default_account.deposit(0)

def test_withdraw_exceptions(default_account):
    with pytest.raises(TypeError):
        default_account.withdraw("100")
    with pytest.raises(ValueError):
        default_account.withdraw(-20)
    with pytest.raises(ValueError):
        default_account.withdraw(2000)  # Перевищує баланс

def test_add_interest_exceptions(default_account):
    with pytest.raises(TypeError):
        default_account.add_interest("5")
    with pytest.raises(ValueError):
        default_account.add_interest(-5)