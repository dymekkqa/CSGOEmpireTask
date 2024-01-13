import pytest
from pages.roulette_page import RoulettePage


class BaseTest:
    roulette_page: RoulettePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.roulette_page = RoulettePage(driver)
