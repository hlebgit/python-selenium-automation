from pages.base_page import Page
from pages.hw4_target_circle_benefits_page import TargetCircleBenefitsPage
from pages.hw4_christmas_tree_product_page import CheckOutChristmasTree
from pages.hw5_product_colors_page import ClickThroughColors
from pages.hw5_product_search_results_page import ProductSearchResults
from pages.hw6_verify_cart_is_empty import VerifyCartIsEmpty

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.target_circle_benefits_page = TargetCircleBenefitsPage(driver)
        self.checkout_christmas_tree_product = CheckOutChristmasTree(driver)
        self.click_through_colors = ClickThroughColors(driver)
        self.product_search_results = ProductSearchResults(driver)
        self.verify_cart_is_empty = VerifyCartIsEmpty(driver)

