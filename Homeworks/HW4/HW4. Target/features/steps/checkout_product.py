from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("Open product page")
def open_product_page(context):
    context.driver.get(
        "https://www.target.com/p/costway-prelit-7-5ft-christmas-tree-flocked-xmas-snowy-tree-450-led-lights/-/A-87791923#lnk=sametab")

@when("Add product to the cart")
def add_product(context):
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test*='AddToCart'] [id*='addToCart']")))
    print("ALL GOOD: ")
    global expected_result
    expected_result = context.driver.find_element(By.XPATH, "//h1[@id='pdp-product-title-id']").text
    context.driver.find_element(By.CSS_SELECTOR, "[class*='AddToCartWrapper'] [id*='addToCart']").click()

@when("Check Out")
def checkout_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/cart']").click()

@then("Verify title")
def view_cart(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='cartItem-title']//div").text
    assert actual_result == expected_result, f'Error! Expected result: {expected_result}; however, actual result is: {actual_result}'