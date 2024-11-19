from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

MOCK_BUN_NAME = 'Булочка'
MOCK_BUN_PRICE = 50
MOCK_INGREDIENT_KETCHUP = {"type":INGREDIENT_TYPE_SAUCE, "name": "Кетчуп", "price": 20}
MOCK_INGREDIENT_CUTLET = {"type":INGREDIENT_TYPE_FILLING, "name": "Котлета", "price": 60}
BURGER_RECEIPT = "(==== Булочка ====)\n" + "= filling Котлета =\n" + "= sauce Кетчуп =\n" + "(==== Булочка ====)\n\n" + "Price: 180"

