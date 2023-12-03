from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class SignInPage(Page):
    ACTUAL_TXT = (By.CSS_SELECTOR, "[class*='AuthHeading'] span")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test*='HeaderPrimary'] [data-test*='AccountLink'] span")
    SIGN_IN_IN_NAV_MENU_BTN = (By.CSS_SELECTOR, "[data-test*='signIn']")
    TERMS_AND_CONDITIONS_BTN = (By.CSS_SELECTOR, "[aria-label*='terms']")

    def verify_sign_in_page_txt(self):
        self.verify_text('Sign into your Target account', *self.ACTUAL_TXT)

    def open_sign_in_page(self):
        self.open_url('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')
        current_url = self.driver.current_url

        if 'login' not in current_url:
            self.click(*self.SIGN_IN_BTN)
            self.click(*self.SIGN_IN_IN_NAV_MENU_BTN)


    def click_terms_and_conditions(self):
        self.driver.find_element(*self.TERMS_AND_CONDITIONS_BTN).click()

    def verify_tnc_page_is_opened(self):
        assert "https://www.target.com/c/terms-conditions" in self.driver.current_url