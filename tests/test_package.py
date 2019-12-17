import pytest

from mypackage import add


@pytest.mark.parametrize('x,y,want',
    [(1, 2, 3), (4, -5, -1), ('4', '5', '45')]
)
def test_add(x, y, want):
    got = add(x, y)
    assert got == want
