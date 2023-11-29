from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
         self.driver.get(url)

    def click(self, *locator):
         self.driver.find_element(*locator).click()

    def find_element(self, *locator):
         return self.driver.find_element(*locator)

    def find_elements(self, *locator):
         return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text,\
            f"Expected text {expected_text} did not match actual {actual_text}"