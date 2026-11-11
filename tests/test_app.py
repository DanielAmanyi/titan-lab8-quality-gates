import pytest
from app import add, classify_score, shipping_cost
def test_add():
    assert add(2, 99) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-5, -5) == -10
def test_classify_score():
    assert classify_score(85) == "excellent"
    assert classify_score(65) == "pass"
    assert classify_score(30) == "fail"

    with pytest.raises(ValueError):
        classify_score(-1)

    with pytest.raises(ValueError):
        classify_score(101)
def test_shipping_cost():
    assert shipping_cost(50) == 8
    assert shipping_cost(100) == 0
    assert shipping_cost(50, priority=True) == 15

    with pytest.raises(ValueError):
        shipping_cost(-1)