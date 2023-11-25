from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClickThroughColors(Page):

    COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
    SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")

    def open_product_page(self):
        self.open_url("https://www.target.com/p/A-88345426")

    def verify_colors(self):
        expected_colors = ['Brown', 'Oatmeal', 'Gray', 'Black']
        actual_colors = []
        self.driver.wait = WebDriverWait(self.driver, 15)
        self.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[alt='Black']")))
        colors = self.driver.find_elements(*self.COLOR_OPTIONS)

        for color in colors:
            color.click()
            selected_color = self.driver.find_element(*self.SELECTED_COLOR).text.split('\n')[1]
            actual_colors.append(selected_color)

        assert expected_colors == actual_colors, f"Expected {expected_colors} did not match actual {actual_colors}"