from pages.base_page import Page
from pages.search_results_page import SearchResults
from selenium.webdriver.common.by import By

class CartPage(SearchResults, Page):
    CART_SUMMARY = (By.CSS_SELECTOR, "[class*='CartSummarySpan']")

    def verify_first_product_was_added(self, amount):
        CART_SUMMARY_TXT = self.find_element(*self.CART_SUMMARY).text
        assert f"{amount} item" in CART_SUMMARY_TXT, f"Expected {amount} item not in {CART_SUMMARY_TXT}"
