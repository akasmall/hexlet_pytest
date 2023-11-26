import pytest
from src.cart import Right
# from src.cart import get_implementations

# make_cart = get_implementations()


# BEGIN (write your solution here)
@pytest.fixture
def add_item_one():
    add_item_one = {'name': 'car', 'price': 3}
    return add_item_one

@pytest.fixture
def add_item_two():
    add_item_one = {'name': 'car', 'price': 10}
    return add_item_one



# def test_right(create_basket):
def test_create_basket(add_item_one, add_item_two):
    # cart = make_cart()
    cart = Right()
    assert cart.items == []
    # cart.add_item({'name': 'car', 'price': 3}, 5)
    cart.add_item(add_item_one, 5)
    assert cart.items[0]['good'] == {'name': 'car', 'price': 3}
    assert cart.items[0]['count'] == 5
    cart.add_item(add_item_two, 2)
    assert cart.items[1]['good'] == {'name': 'car', 'price': 10}
    assert cart.items[1]['count'] == 2
    
# END
