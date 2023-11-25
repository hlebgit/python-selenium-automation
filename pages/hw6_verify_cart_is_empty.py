from pages.base_page import Page
from selenium.webdriver.common.by import By

class VerifyCartIsEmpty(Page):

    def open_target(self):
        self.open_url("https://www.target.com/")

    def click_on_cart_icon(self):
        self.click(By.CSS_SELECTOR, "[data-test='@web/CartIcon'] image")

    def verify_cart_is_empty_message(self):
        expected_result = "Your cart is empty"
        actual_result = self.find_element(By.CSS_SELECTOR, "[data-test='emptyCartContainer'] h1").text

        assert actual_result == expected_result, f"Error: 'Your cart is empty' message is not shown!!"

