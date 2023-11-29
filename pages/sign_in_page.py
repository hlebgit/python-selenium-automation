from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    ACTUAL_TXT = (By.CSS_SELECTOR, "[class*='AuthHeading'] span")
    def verify_sign_in_page_txt(self):
        self.verify_text('Sign into your Target account', *self.ACTUAL_TXT)