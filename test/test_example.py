import pytest
from pyDFT import example


def test_double():
    """
    Test that we can double an integer

    """
    assert example.double(1) == 2


def test_double_str():
    """
    Test that trying to double a string raises the right error

    """
    with pytest.raises(ValueError):
        example.double("foo")
