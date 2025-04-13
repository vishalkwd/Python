import pytest
from chubb import intelligent_substring

def test_intelligent_substring_prime_word(capsys):
    # Arrange
    values = '00010100001000000000000001'
    k = 1
    string = 'abcd'

    # Act
    intelligent_substring(values, k, string)

    # Assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "Prime word"

def test_intelligent_substring_standard(capsys):
    # Arrange
    values = '00010100001000000000000001'
    k = 5
    string = 'abcd'

    # Act
    intelligent_substring(values, k, string)

    # Assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "Standard"

def test_intelligent_substring_empty_string(capsys):
    # Arrange
    values = '00010100001000000000000001'
    k = 0
    string = ''

    # Act
    intelligent_substring(values, k, string)

    # Assert
    captured = capsys.readouterr()
    assert captured.out.strip() == "Prime word"

def test_intelligent_substring_invalid_values_length():
    # Arrange
    values = '000101'
    k = 2
    string = 'abcd'

    # Act & Assert
    with pytest.raises(ValueError, match="The length of values must be 26."):
        intelligent_substring(values, k, string)