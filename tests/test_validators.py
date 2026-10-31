import pytest

from userval import MAX_LENGTH, validate_username


def test_valid_username_is_returned():
    assert validate_username("alice") == "alice"


def test_surrounding_whitespace_is_stripped():
    assert validate_username("  bob  ") == "bob"


def test_max_length_is_allowed():
    name = "a" * MAX_LENGTH
    assert validate_username(name) == name


def test_too_long_is_rejected():
    with pytest.raises(ValueError):
        validate_username("a" * (MAX_LENGTH + 1))


def test_none_is_rejected():
    with pytest.raises(ValueError):
        validate_username(None)


def test_non_string_is_rejected():
    with pytest.raises(ValueError):
        validate_username(123)


def test_empty_string_is_rejected():
    with pytest.raises(ValueError):
        validate_username("")


def test_whitespace_only_is_rejected():
    with pytest.raises(ValueError):
        validate_username("   ")
