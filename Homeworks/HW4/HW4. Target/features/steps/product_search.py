from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open product page")
def open_product_page(context):
    context.driver.get("https://www.target.com/p/7-5-39-pre-lit-virginia-pine-artificial-christmas-tree-dual-color-lights-wondershop-8482/-/A-87305103#lnk=sametab")

@when("Add product to the cart")
def add_product(context):
    sleep(5)
    global expected_result
    expected_result = context.driver.find_element(By.XPATH, "//h1[@id='pdp-product-title-id']").text
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test*='order'] [id*='addToCartButton']").click()

@when("Check Out")
def checkout_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()

@then("Verify title")
def view_cart(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='cartItem-title']//div").text
    assert actual_result == expected_result, f'Error! Expected result: {expected_result}; however, actual result is: {actual_result}'