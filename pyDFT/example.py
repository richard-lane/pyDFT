"""
An example of a bit of code

"""


def double(x: int) -> int:
    # This string documents the function; this is the reST format which PyCharm will autofill by default
    """
    This is a function, it doubles x and then returns the value

    The syntax x: int is a type hint - it means x should be an int
    The synax -> int means this function returns an int

    :param x: the number that we want to double
    :returns: x but doubled
    :raises: ValueError if x is not an integer

    """
    # Check arguments are sensible
    if not isinstance(x, int):
        raise ValueError(f"x must be an integer; {x} is invalid")

    return x * 2
