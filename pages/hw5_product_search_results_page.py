from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductSearchResults(Page):
    def open_target(self):
        self.open_url("https://www.target.com/")

    def search_product(self, product_name):
        self.input(product_name, By.ID, "search")
        self.click(By.CSS_SELECTOR, "[data-test*='SearchButton']")

    def verify_product(self):
        images = []
        image_src = self.find_elements(
            By.CSS_SELECTOR,
            "[data-test*='ProductCardWrapper'] [data-test*='ProductCardImage/primary'] img")

        for img in image_src:
            images.append(img.get_attribute("src"))

        print("Images count: ", len(images))

        products = []
        product_name = self.find_elements(By.CSS_SELECTOR, "[class*='ProductCardItemInfoDiv'] a[aria-label]")

        for product in product_name:
            products.append(product.text)

        print("Product name count: ", len(products))

        assert len(images) == len(products), f'Count of product names is {len(products)}, ' \
                                             f'while count of product images is {len(images)}!! ' \
                                             f'Some products do not have name or image!!'
