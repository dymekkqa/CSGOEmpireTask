import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RoulettePage(BasePage):
    PAGE_URL = Links.ROULETTE_PAGE
    INPUT_AMOUNT = ("xpath", "//input[@placeholder='Enter bet amount...']")
    CLEAR_AMOUNT = ("xpath", "//button[@type='button' and text()='Clear']")

    def add_amount_value(self, amount):
        with allure.step(f"Input amount value {amount} to amount field"):
            self.wait.until(EC.element_to_be_clickable(self.INPUT_AMOUNT)).send_keys(amount)

    def clear_amount_field(self):
        with allure.step("Clear amount field"):
            self.wait.until(EC.element_to_be_clickable(self.CLEAR_AMOUNT)).click()

    def check_amount_field(self):
        value = self.wait.until(EC.element_to_be_clickable(self.INPUT_AMOUNT)).get_attribute("value")
        with allure.step(f"Check amount value {value}"):
            return str(value)