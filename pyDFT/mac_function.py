

def roman_numeral(s: str) -> int:
    """ Takes a roman numeral, entered as 's' a string, and returns the corresponding
    value as an integer


    """
    if s == 'I':
        return 1
    if s == 'IV':
        return 4
    if s == 'V':
        return 5
    if s == 'X':
        return 10

    if not isinstance(s, str):
        raise ValueError(f"x must be a string; {s} is invalid")
    while s != 'I' and s !='IV' and s!= 'V' and s != 'X':
        raise ValueError(f"Invalid choice of numeral, must be I, IV, V or X")


