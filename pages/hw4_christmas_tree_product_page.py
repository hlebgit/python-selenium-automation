from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckOutChristmasTree(Page):
    def open_christmas_tree_page(self):
        self.open_url('https://www.target.com/p/costway-prelit-7-5ft-christmas-tree-flocked-xmas-snowy-tree-450-led-lights/-/A-87791923#lnk=sametab')

    def add_product_to_the_cart(self):
        self.driver.wait = WebDriverWait(self.driver, 15)
        self.driver.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test*='AddToCart'] [id*='addToCart']")))
        global expected_result
        expected_result = self.find_element(By.XPATH, "//h1[@id='pdp-product-title-id']").text
        self.click(By.CSS_SELECTOR, "[class*='AddToCartWrapper'] [id*='addToCart']")

    def checkout_cart(self):
        self.click(By.CSS_SELECTOR, "[href='/cart']")

    def view_cart_and_verify(self):
        actual_result = self.find_element(By.XPATH, "//div[@data-test='cartItem-title']//div").text
        assert actual_result == expected_result, f'Error! Expected result: {expected_result}; however, actual result is: {actual_result}'