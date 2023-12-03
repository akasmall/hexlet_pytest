# cart = make_cart()
# cart.add_item({'name': 'car', 'price': 3}, 5)
# cart.add_item({'name': 'house', 'price': 10}, 2)
# len(cart.get_items())  # 2
# cart.get_cost()  # 35
# # Считаем, что все товары уникальные
# # Товар с таким же названием добавляется в корзину новой позицией
# cart.add_item({'name': 'house', 'price': 10}, 1)
# len(cart.get_items())  # 3
# cart.get_cost()  # 45
from src.cart import Right, Wrong1, Wrong2, Wrong3
# from src.cart import get_implementations

# make_cart = get_implementations()


def test_right():
    cart = Right()
    assert not len(cart.get_items())
    cart.add_item({'name': 'car', 'price': 3}, 5)
    cart.add_item({'name': 'house', 'price': 10}, 2)
    assert cart.get_items() == [
        {'good': {'name': 'car', 'price': 3}, 'count': 5},
        {'good': {'name': 'house', 'price': 10}, 'count': 2}
        ]
    assert len(cart.get_items()) == 2
    assert cart.get_cost() == 35
    cart.add_item({'name': 'house', 'price': 10}, 1)
    assert len(cart.get_items()) == 3
    assert cart.get_cost() == 45

def test_wrong1():
    cart = Wrong1()
    assert cart.items == []
    cart.add_item({'name': 'car', 'price': 3}, 5)
    cart.add_item({'name': 'house', 'price': 10}, 2)
    assert cart.get_cost() != 35
    cart.add_item({'name': 'house', 'price': 10}, 1)
    assert cart.get_cost() != 45

def test_wrong2():
    cart = Wrong2()
    assert cart.items == []
    cart.add_item({'name': 'car', 'price': 3}, 5)
    cart.add_item({'name': 'house', 'price': 10}, 2)
    assert len(cart.get_items()) != 2
    cart.add_item({'name': 'house', 'price': 10}, 1)
    assert len(cart.get_items()) != 3

def test_wrong3():
    cart = Wrong3()
    assert cart.items == []
    cart.add_item({'name': 'car', 'price': 3}, 5)
    cart.add_item({'name': 'house', 'price': 10}, 2)
    assert cart.get_count() != 7
    cart.add_item({'name': 'house', 'price': 10}, 1)
    assert cart.get_count() != 8    
# END

'''
# BEGIN
# mentor - учитель
def test_cart():
    cart = make_cart()
    assert not len(cart.get_items())

    cart.add_item({'name': 'car', 'price': 3}, 5)
    assert len(cart.get_items()) == 1
    assert cart.get_cost() == 15
    assert cart.get_count() == 5

    cart.add_item({'name': 'house', 'price': 10}, 2)
    assert len(cart.get_items()) == 2
    assert cart.get_cost() == 35
    assert cart.get_count() == 7
# END
'''