from pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR, "#search")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test*='SearchButton']")

    def open_main(self):
        self.open_url('https://www.target.com/')

    def search_product_on_main_page(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def sign_in(self):
        self.click(By.CSS_SELECTOR, "[data-test*='AccountLink'] span")

    def sign_in_in_nav_manu(self):
        self.click(By.CSS_SELECTOR, "[data-test*='signIn']")

