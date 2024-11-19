import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize('expected_price',
                             [20, 20.50])
    def test_get_ingredient_price(self, expected_price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Кетчуп", expected_price)
        ingredient_price = ingredient.get_price()
        assert ingredient_price == expected_price

    def test_get_ingredient_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Кетчуп", 20)
        ingredient_name = ingredient.get_name()
        assert ingredient_name == "Кетчуп"

    @pytest.mark.parametrize('expected_ingredient_type',
                             [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_ingredient_type(self, expected_ingredient_type):
        ingredient = Ingredient(expected_ingredient_type, "Ингредиент", 50)
        ingredient_type = ingredient.get_type()
        assert ingredient_type == expected_ingredient_type