import pytest
from unittest.mock import Mock
from data import MOCK_BUN_NAME,MOCK_BUN_PRICE,MOCK_INGREDIENT_CUTLET, MOCK_INGREDIENT_KETCHUP
from praktikum.burger import Burger


@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = MOCK_BUN_NAME
    mock_bun.price = MOCK_BUN_PRICE
    mock_bun.get_name.return_value = MOCK_BUN_NAME
    mock_bun.get_price.return_value = MOCK_BUN_PRICE
    return mock_bun

@pytest.fixture()
def mock_ingredient_cutlet():
    mock_ingredient_cutlet = Mock()
    mock_ingredient_cutlet.type = MOCK_INGREDIENT_CUTLET["type"]
    mock_ingredient_cutlet.name = MOCK_INGREDIENT_CUTLET["name"]
    mock_ingredient_cutlet.price = MOCK_INGREDIENT_CUTLET["price"]
    mock_ingredient_cutlet.get_type.return_value = MOCK_INGREDIENT_CUTLET["type"]
    mock_ingredient_cutlet.get_name.return_value = MOCK_INGREDIENT_CUTLET["name"]
    mock_ingredient_cutlet.get_price.return_value = MOCK_INGREDIENT_CUTLET["price"]
    return mock_ingredient_cutlet

@pytest.fixture()
def mock_ingredient_ketchup():
    mock_ingredient_ketchup = Mock()
    mock_ingredient_ketchup.type = MOCK_INGREDIENT_KETCHUP["type"]
    mock_ingredient_ketchup.name = MOCK_INGREDIENT_KETCHUP["name"]
    mock_ingredient_ketchup.price = MOCK_INGREDIENT_KETCHUP["price"]
    mock_ingredient_ketchup.get_type.return_value = MOCK_INGREDIENT_KETCHUP["type"]
    mock_ingredient_ketchup.get_name.return_value = MOCK_INGREDIENT_KETCHUP["name"]
    mock_ingredient_ketchup.get_price.return_value = MOCK_INGREDIENT_KETCHUP["price"]
    return mock_ingredient_ketchup

@pytest.fixture()
def make_burger(mock_bun, mock_ingredient_cutlet, mock_ingredient_ketchup):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_cutlet)
    burger.add_ingredient(mock_ingredient_ketchup)
    return burger
