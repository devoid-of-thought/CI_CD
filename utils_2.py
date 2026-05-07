"""Converts int between 0 and 100 to binary"""


def conversion(a: int) -> bin:
    """Converts int between 0 and 100 to binary"""
    if a < 0:
        raise ValueError("Input must be a non-negative integer")
    if a > 100:
        raise ValueError("Input must be less than or equal to 100")
    if int(a) != a:
        raise ValueError("Input must be an integer")
    return bin(a)
