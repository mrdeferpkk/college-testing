import pytest
from src.temperature_converter import TemperatureConverter


def test_zero_celsius_is_32_fahrenheit():
    result = TemperatureConverter.celsius_to_fahrenheit(0)
    assert result == pytest.approx(32.0)


def test_100_celsius_is_212_fahrenheit():
    result = TemperatureConverter.celsius_to_fahrenheit(100)
    assert result == pytest.approx(212.0)


def test_32_fahrenheit_is_zero_celsius():
    result = TemperatureConverter.fahrenheit_to_celsius(32)
    assert result == pytest.approx(0.0)


def test_212_fahrenheit_is_100_celsius():
    result = TemperatureConverter.fahrenheit_to_celsius(212)
    assert result == pytest.approx(100.0)


@pytest.mark.parametrize("invalid_input", ["abc", None, [1, 2], True])
def test_celsius_invalid_type_raises_type_error(invalid_input):
    with pytest.raises(TypeError, match="Temperature must be a number"):
        TemperatureConverter.celsius_to_fahrenheit(invalid_input)


def test_celsius_below_absolute_zero_raises_error():
    with pytest.raises(ValueError, match="Temperature below absolute zero"):
        TemperatureConverter.celsius_to_fahrenheit(-300)


def test_fahrenheit_below_absolute_zero_raises_error():
    with pytest.raises(ValueError, match="Temperature below absolute zero"):
        TemperatureConverter.fahrenheit_to_celsius(-500)