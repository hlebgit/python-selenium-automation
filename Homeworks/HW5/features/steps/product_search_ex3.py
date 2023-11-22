from behave import given, when, then
from selenium.webdriver.common.by import By


@given("Open target")
def open_target(context):
    context.driver.get("https://www.target.com/")


@when("Search for {product_name}")
def search_product(context, product_name):
    context.driver.find_element(By.ID, "search").send_keys(product_name)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test*='SearchButton']").click()


@then("Verify product name and image")
def verify_product(context):
    images = []
    image_src = context.driver.find_elements(
        By.CSS_SELECTOR,
        "[data-test*='ProductCardWrapper'] [data-test*='ProductCardImage/primary'] img")

    for img in image_src:
        images.append(img.get_attribute("src"))

    print("Images count: ", len(images))

    products = []
    product_name = context.driver.find_elements(By.CSS_SELECTOR, "[class*='ProductCardItemInfoDiv'] a[aria-label]")

    for product in product_name:
        products.append(product.text)

    print("Product name count: ", len(products))

    assert len(images) == len(products), f'Count of product names is {len(products)}, ' \
                                         f'while count of product images is {len(images)}!! ' \
                                        f'Some products do not have name or image!!'
