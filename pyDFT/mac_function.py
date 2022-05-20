def roman_numeral(s: str) -> int:
    """
    :param s: string to parse as a roman numeral
    :returns: value of s as an integer

    """
    if not isinstance(s, str):
        raise ValueError(f"x must be a string; {s} is invalid")
    if not s in {"I", "IV", "V", "X"}:
        raise ValueError(f"Invalid choice of numeral, must be I, IV, V or X")

    if s == "I":
        return 1
    if s == "IV":
        return 4
    if s == "V":
        return 5
    if s == "X":
        return 10
