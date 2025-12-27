import pytest

from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   Skypro", "Skypro")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Skypro Skypro", "Skypro Skypro"),
    ("Skypro  ", "Skypro  ")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Skypro", "S"),
    ("12345", "3")
])
def test_contains_positive(input_str, expected):
    assert string_utils.contains(input_str, expected) is True


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   ", "f"),
    ("", "f")
])
def test_contains_negative(input_str, expected):
    assert not string_utils.contains(input_str, expected)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "k", "Sypro"),
    ("Skypro", "pro", "Sky")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("World", "ld", "World")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert not string_utils.delete_symbol(input_str, symbol) == expected
