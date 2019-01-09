import pytest

from missing_integer import find_missing_integer


@pytest.mark.parametrize(
    'array_numbers, expected',
    [
        (
            [3, 1, 2, 4, 6], 5
        ),
        (
            [1, 1, 2, 4], 3
        ),
        (
            [1, 2, 4], 3
        ),
        (
            [2, 3, 4, 5, 7, 6], 1
        )
    ]
)
def test_equilibrium_naturals(array_numbers, expected):
    assert expected == find_missing_integer(array_numbers)
