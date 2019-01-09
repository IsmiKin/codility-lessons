import pytest

from equilibrium import find_equilibrium_naturals, find_equilibrium_integers


@pytest.mark.parametrize(
    'array_numbers, expected',
    [
        (
            [3, 1, 2, 4, 3], 1
        ),
        (
            [1, 10, 2, 5], 4
        ),
        (
            [10, 85, 30, 3], 62
        ),
        (
            [1, 1, 1, 1, 10], 6
        ),
        (
            [1, 1, 1, 1, 10], 6
        )
    ]
)
def test_equilibrium_naturals(array_numbers, expected):
    assert expected == find_equilibrium_naturals(array_numbers)


@pytest.mark.parametrize(
    'array_numbers, expected',
    [
        (
            [1, 1, 1, 1, -10], 6
        ),
        (
            [1, 10, 2, 5], 4
        ),
        (
            [10, 85, 30, 3], 62
        ),
        (
            [1, 1, 1, 1, 10], 6
        ),
        (
            [1, 1, 1, 1, 10], 6
        ),
        (
            [-1, 2, 4, -2, 5, -1, -6], 1
        )

    ]
)
def test_equilibrium_integers(array_numbers, expected):
    assert expected == find_equilibrium_integers(array_numbers)
