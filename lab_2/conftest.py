import pytest
from src.main import BankAccount

@pytest.fixture
def default_account():
    """Фікстура, що повертає готовий банківський рахунок для тестів."""
    return BankAccount("Олександр", 1000.0)