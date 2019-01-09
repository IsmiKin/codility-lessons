import pytest

from brackets import is_properly_nested


@pytest.mark.parametrize(
    'string, expected',
    [
        (
            '([{}[]])', True
        ),
        (
            '([{}[(])])', False
        ),
        (
            '((((([[{}]][[[]]])))))', True
        )
    ]
)
def test_is_properly_nested(string, expected):
    assert expected == is_properly_nested(string)
