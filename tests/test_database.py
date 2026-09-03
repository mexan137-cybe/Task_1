from database import Database
class TestDatabase:

    def test_available_buns_count_buns(self):
        db = Database()
        assert len(db.available_buns()) == 3

    def test_available_buns_first_bun(self):
        db = Database()
        first_bun = db.available_buns()[0]
        assert first_bun.get_name() == 'black bun' and first_bun.get_price() == 100 # Не решил .get_name() или .name

    def test_available_buns_last_bun(self):
        db = Database()
        last_bun = db.available_buns()[-1]
        assert last_bun.get_name() == "red bun" and last_bun.get_price() == 300

    def test_available_ingredients_returns_correct_count(self):
        db = Database()
        assert len(db.available_ingredients()) == 6

    def test_available_ingredients_contains_sauce_first(self):
        db = Database()
        first_ingredient = db.available_ingredients()[0]
        assert (first_ingredient.get_name() == "hot sauce" and first_ingredient.get_price() == 100)

    def test_available_ingredients_contains_filling_last(self):
        db = Database()
        last_ingredient = db.available_ingredients()[-1]
        assert (last_ingredient.get_name() == "sausage" and last_ingredient.get_price() == 300)
