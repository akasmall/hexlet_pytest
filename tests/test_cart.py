from hexlet_pytest.cart import get_implementations
cart_list = []

make_cart = get_implementations()


# BEGIN (write your solution here)
# @pytest.fixture
def test_make_cart():
    assert make_cart() == cart_list
# END
