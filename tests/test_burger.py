from praktikum.burger import Burger
from data import MOCK_BUN_PRICE,MOCK_INGREDIENT_CUTLET, MOCK_INGREDIENT_KETCHUP, BURGER_RECEIPT

class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient_cutlet):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_cutlet)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, mock_ingredient_cutlet):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_cutlet)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, mock_ingredient_cutlet, mock_ingredient_ketchup):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_cutlet)
        burger.add_ingredient(mock_ingredient_ketchup)
        burger.move_ingredient(0,1)
        assert burger.ingredients[1] == mock_ingredient_cutlet

    def test_get_burger_price(self, make_burger):
        burger = make_burger
        burger_price = burger.get_price()
        expected_price = 2 * MOCK_BUN_PRICE + MOCK_INGREDIENT_CUTLET['price'] + MOCK_INGREDIENT_KETCHUP['price']
        assert burger_price == expected_price

    def test_get_burger_receipt(self, make_burger):
        burger = make_burger
        burger_receipt = burger.get_receipt()
        assert burger_receipt == BURGER_RECEIPT







