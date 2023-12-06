from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep

class TargetHelpPage(Page):
    HELP_DROPDOWN_SELECT = (By.CSS_SELECTOR, "[name*='viewHelp']")
    HELP_DROPDOWN_OPTION = (By.CSS_SELECTOR, "[value='Gift Cards']")

    def choose_help_dropdown_option(self, topic):
        dropdown_select = self.find_element(*self.HELP_DROPDOWN_SELECT)
        dropdown_option = self.find_element(*self.HELP_DROPDOWN_OPTION).text

        select = Select(dropdown_select)
        select.select_by_value(topic)
