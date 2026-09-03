import pytest
from unittest.mock import Mock
from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE

class TestBurger:

    def test_init_empty_burger(self):
        empty_burger = Burger()
        assert empty_burger.bun is None and empty_burger.ingredients == []

    def test_set_buns_add_buns(self):
        mock_buns = Mock()
        mock_buns.name = 'Моковая булочка'
        empty_burger = Burger()
        empty_burger.set_buns(mock_buns)
        assert mock_buns == empty_burger.bun

    def test_add_ingredient_add_value(self):
        mock_ingredient = Mock() 
        empty_burger = Burger()
        empty_burger.add_ingredient(mock_ingredient) # Кладем "объект" ингридиента в бургер
        assert mock_ingredient in empty_burger.ingredients

    def test_add_ingredient_append_value(self):
        mock_ingredient = Mock() 
        empty_burger = Burger()
        empty_burger.add_ingredient(mock_ingredient) 
        empty_burger.add_ingredient(mock_ingredient) 
        assert len(empty_burger.ingredients) == 2

    def test_remove_ingredient_remove_from_list(self):
        mock_ingredient_1, mock_ingredient_2, mock_ingredient_3 = Mock(), Mock(), Mock() 
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1) 
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger.remove_ingredient(1)
        assert burger.ingredients == [mock_ingredient_1, mock_ingredient_3]

    def test_move_ingredient_move_from_list(self):
        mock_ingredient_1, mock_ingredient_2, mock_ingredient_3 = Mock(), Mock(), Mock() 
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1) 
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger.move_ingredient(0,2)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_3, mock_ingredient_1]

    def test_get_price_calculate(self):
        mock_buns = Mock()
        mock_buns.get_price.return_value = 105.5
        mock_ingredient_1, mock_ingredient_2 = Mock(), Mock()
        mock_ingredient_1.get_price.return_value = 30.5
        mock_ingredient_2.get_price.return_value = 8.5
        burger = Burger()
        burger.set_buns(mock_buns)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        assert burger.get_price() == 250.0

    def test_get_receipt_return_final_price(self):
        mock_buns = Mock()
        mock_buns.get_price.return_value = 50.0
        burger = Burger()
        burger.set_buns(mock_buns)
        assert "Price: 100.0" in burger.get_receipt()

    def test_get_receipt_return_buns(self):
        mock_buns = Mock()
        mock_buns.get_price.return_value = 50.0
        mock_buns.get_name.return_value = 'Булка с космической пылью'
        burger = Burger()
        burger.set_buns(mock_buns)
        assert 'Булка с космической пылью' in burger.get_receipt()

    def test_get_receipt_return_ingredient(self):
        mock_buns = Mock()
        mock_buns.get_price.return_value = 50
        mock_buns.get_name.return_value = 'Булка с космической пылью'

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Соус из космонавтов'
        mock_ingredient.get_price.return_value = 20
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        burger = Burger()
        burger.set_buns(mock_buns)
        burger.add_ingredient(mock_ingredient)
        assert 'sauce Соус из космонавтов' in burger.get_receipt()
        