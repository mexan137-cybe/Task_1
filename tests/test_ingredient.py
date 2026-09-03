import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestIngredient:

    def test_init_set_name(self):
        name = "Паштет из утки"
        price = 55.5
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, price)
        assert ingredient.name == name

    def test_init_set_price(self):
        name = "Паштет из утки"
        price = 150.0
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name, price)
        assert ingredient.price == price

    def test_get_name_returns_expected_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Паштет из утки", 80.0)
        assert ingredient.get_name() == "Паштет из утки"

    def test_get_price_returns_expected_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING ,"Паштет из утки", 80.0)
        assert ingredient.get_price() == 80.0

    def test_get_type_returns_expected_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING ,"Паштет из утки", 80.0)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

    @pytest.mark.parametrize("name, price",[("Бесплатная", 0.0),("Минусовая", -50.0),("", 99.99)])
    def test_bun_creation_with_various_data(self, name, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE ,name, price)
        assert ingredient.get_name() == name and ingredient.get_price() == price