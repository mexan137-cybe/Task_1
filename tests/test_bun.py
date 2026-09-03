import pytest
from bun import Bun

class TestBun:

    def test_init_set_name(self):
        name = "Кунжутный астероид"
        price = 100.5
        bun = Bun(name, price)
        assert bun.name == name

    def test_init_set_price(self):
        name = "Кунжутный астероид"
        price = 150.0
        bun = Bun(name, price)
        assert bun.price == price

    def test_get_name_returns_expected_value(self):
        bun = Bun("Кунжутный астероид", 80.0)
        assert bun.get_name() == "Кунжутный астероид"

    def test_get_price_returns_expected_value(self):
        bun = Bun("Кунжутный астероид", 120.99)
        assert bun.get_price() == 120.99

    @pytest.mark.parametrize("name, price",[("Бесплатная", 0.0),("Минусовая", -50.0),("", 99.99)])
    def test_bun_creation_with_various_data(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name and bun.get_price() == price
