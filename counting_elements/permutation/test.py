import pytest

from permutation import is_permutation


@pytest.mark.parametrize(
    'array_numbers, expected',
    [
        (
            [3, 1, 2, 4], True
        ),
        (
            [1, 1, 2, 4], False
        ),
        (
            [1, 2, 4], False
        ),
        (
            [2, 3, 4, 5, 7, 6], True
        )
    ]
)
def test_equilibrium_naturals(array_numbers, expected):
    assert expected is is_permutation(array_numbers)
