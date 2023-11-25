from pages.base_page import Page
from selenium.webdriver.common.by import By
class TargetCircleBenefitsPage(Page):

    def open_target_circle_benefits_page(self):
        self.open_url('https://www.target.com/circle')

    def verify_target_circle_benefits(self, number_of_benefits):
        number_of_benefits = int(number_of_benefits)
        elements = self.find_elements(By.CSS_SELECTOR, "[class*='BenefitsGrid'] li")
        assert len(elements) == number_of_benefits,\
            f"Error: required benefits should be {number_of_benefits}, actual number is {len(elements)}!"