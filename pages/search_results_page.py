from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SearchResults(Page):
    ADD_FIRST_PRODUCT_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    ADD_PRODUCT_BTN = (By.CSS_SELECTOR, "[data-test*='FulfillmentSection'] [id*='addToCartButton']")
    TITLE_OF_FIRST_PRODUCT_FROM_SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-test='product-title']")
    VIEW_CART_BTN = (By.CSS_SELECTOR, "[href='/cart']")
    def add_first_product_of_search_results_to_the_cart(self):
        sleep(5)
        print("TITLE: \n", self.find_element(*self.TITLE_OF_FIRST_PRODUCT_FROM_SEARCH_RESULTS).text)
        actual_result = self.find_element(*self.ADD_FIRST_PRODUCT_TO_CART_BTN).text
        expected_result = 'Add to cart'

        # Check if product can be added to the cart OR delivered only
        assert actual_result == expected_result,\
            f"Expected text button is {expected_result};\n"\
            f"Actual text button is {actual_result}."

        print("Here: \n\n", self.find_element(*self.ADD_FIRST_PRODUCT_TO_CART_BTN).text)
        self.click(*self.ADD_FIRST_PRODUCT_TO_CART_BTN)
        sleep(2)
        self.click(*self.ADD_PRODUCT_BTN)


    def click_view_cart_and_checkout(self):
        self.click(*self.VIEW_CART_BTN)
