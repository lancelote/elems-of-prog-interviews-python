import pytest

from src.primitive_types.count_bits import count_bits


@pytest.mark.parametrize(
    "x,expected_count",
    [
        (0, 0),
        (42, 3),
        (7, 3),
        (128, 1),
    ],
)
def test_count_bits(x, expected_count):
    assert count_bits(x) == expected_count
