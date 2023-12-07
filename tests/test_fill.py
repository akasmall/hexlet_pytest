import pytest
from src.fill import fill


@pytest.fixture(name='collection')
def _collection():
    return [1, 2, 3, 4]


def test_fill(collection):
    fill(collection, '*', 1, 3)
    assert collection == [1, '*', '*', 4]


# BEGIN (write your solution here)
def test_fill_extreme_conditions_w1(collection):
    fill(collection, None)
    assert collection == [1, 2, 3, 4]


def test_fill_extreme_conditions_w2(collection):
    fill(collection, '*')
    assert collection == ['*', '*', '*', '*']


def test_fill_extreme_conditions_w3(collection):
    fill(collection, '*', 1)
    assert collection == [1, '*', '*', '*']

