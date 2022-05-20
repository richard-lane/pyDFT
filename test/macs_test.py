import pytest
from pyDFT import mac_function


def test_numeral():

    """
    Test the assigned numeral string is returned as an integer
    :return:
    """

    assert mac_function.roman_numeral("I") == 1


def test_int():
    """
    Test value error raised if int is used

    :return:
    """
    with pytest.raises(ValueError):
        mac_function.roman_numeral(1)


def test_incorrect_str():
    """
    Test if a numeral outside specified value is use it raises an error

    """
    with pytest.raises(ValueError):
        mac_function.roman_numeral("VI")
