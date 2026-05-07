import utils_2
import pytest


@pytest.mark.parametrize(
    "a, expected",
    [
        (0, "0b0"),
        (1, "0b1"),
        (2, "0b10"),
        (10, "0b1010"),
        (100, "0b1100100"),
    ],
)
def test_conversion(a, expected):
    result = utils_2.conversion(a)
    assert result == expected


@pytest.mark.parametrize(
    "a",
    [-1, 101, 3.5],
)
def test_conversion_invalid_input(a):
    with pytest.raises(ValueError):
        utils_2.conversion(a)
