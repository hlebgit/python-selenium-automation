from pages.base_page import Page
from pages.hw4_target_circle_benefits_page import TargetCircleBenefitsPage
from pages.hw4_christmas_tree_product_page import CheckOutChristmasTree
from pages.hw5_product_colors_page import ClickThroughColors
from pages.hw5_product_search_results_page import ProductSearchResults
from pages.hw6_verify_cart_is_empty import VerifyCartIsEmpty
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.cart_page import CartPage
from pages.search_results_page import SearchResults
from pages.target_help_page import TargetHelpPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.target_circle_benefits_page = TargetCircleBenefitsPage(driver)
        self.checkout_christmas_tree_product = CheckOutChristmasTree(driver)
        self.click_through_colors = ClickThroughColors(driver)
        self.product_search_results = ProductSearchResults(driver)
        self.verify_cart_is_empty = VerifyCartIsEmpty(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.cart_page = CartPage(driver)
        self.search_results_page = SearchResults(driver)
        self.target_help_page = TargetHelpPage(driver)


