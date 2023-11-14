from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

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


#Exercise 3
@when('Click sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('Click sign in navigation menu')
def click_sign_in_in_nav_manu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()

@then('Verify sign in page opened')
def check_page(context):
    expected_result = 'Sign into your HW4. Target account'
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your HW4. Target account']").text
    assert expected_result == actual_result, "Error! Results are not equal!"