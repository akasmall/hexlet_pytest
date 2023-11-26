# BEGIN (write your solution here)
def test_create_basket():
    cart = make_cart()
    assert cart.items == []
    cart.add_item({'name': 'car', 'price': 3}, 5)
    assert cart.items[0]['good'] == {'name': 'car', 'price': 3}
    assert cart.items[0]['count'] == 5
    cart.add_item({'name': 'car', 'price': 10}, 2)
    assert cart.items[1]['good'] == {'name': 'car', 'price': 10}
    assert cart.items[1]['count'] == 2

# END
