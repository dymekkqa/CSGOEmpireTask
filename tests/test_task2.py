import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Task 2")
class TestClearing(BaseTest):

    @allure.title("Clear amount input")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_amount_value_from_amount_input(self):
        self.roulette_page.open()
        self.roulette_page.is_opened()
        self.roulette_page.add_amount_value(1)
        self.roulette_page.clear_amount_field()
        assert self.roulette_page.check_amount_field() == "0,00"


