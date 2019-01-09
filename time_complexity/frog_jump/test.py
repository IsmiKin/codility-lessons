import pytest

from frog_jump import jumping


@pytest.mark.parametrize(
    'initial, destination, step, expected',
    [
        (
            [1, 10, 2, 5]
        ),
        (
            [10, 85, 30, 3]
        )
    ]
)
def test_frog_1(initial, destination, step, expected):
    assert expected == jumping(initial, destination, step)
