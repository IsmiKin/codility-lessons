import pytest

from max_product import max_product_of_three


@pytest.mark.parametrize(
    'array, expected',
    [
        (
            [-3, 1, 2, -2, 5, 6], 60
        ),
        (
            [-2, 1, 5, 0, 2, -3], 30
        ),
        (
            [-2, 1, -5, 0, 2, -3], 30
        )
    ]
)
def test_max_product_of_three(array, expected):
    assert expected == max_product_of_three(array)
