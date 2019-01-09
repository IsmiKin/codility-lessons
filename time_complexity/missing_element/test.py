import pytest

from missing_element import find_missing_element


@pytest.mark.parametrize(
    'array_elements',
    [
        (
            [1, 2, 4, 5]
        )
    ]
)
def test_find_missing_element_1(array_elements):
    expected = 3
    result = find_missing_element(array_elements)

    assert expected == result
