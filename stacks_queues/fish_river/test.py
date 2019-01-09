import pytest

from fish_river import fish_alives_in_river


@pytest.mark.parametrize(
    'fish_sizes, fish_directions, expected',
    [
        (
            [4, 3, 2, 1, 5], [0, 1, 0, 0, 0], [4, 5]
        ),
        (
            [6, 3, 2, 1, 4, 5, 7], [1, 1, 0, 0, 0, 0, 0], [7]
        )
    ]
)
def test_fish_alives_in_river(fish_sizes, fish_directions, expected):
    assert expected == fish_alives_in_river(fish_sizes, fish_directions)
