from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open HW4. Target page')
def open_target(context):
    context.driver.get('https://www.target.com')


@when('Click cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon'] [href*='#Cart']").click()


@then('Empty cart message is shown')
def check_message(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem' and text()='Your cart is empty']").text
    assert expected_result == actual_result, "Error! Results are not equal!"