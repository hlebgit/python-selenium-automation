from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

COLOR_OPTIONS = (By. CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given("Open target page with product 'Sweater'")
def open_product_page(context):
    context.driver.get("https://www.target.com/p/A-88345426")


@then("Verify user can click through colors")
def verify_colors(context):
    expected_colors = ['Brown', 'Oatmeal', 'Gray', 'Black']
    actual_colors = []
    context.driver.wait = WebDriverWait(context.driver, 15)
    context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[alt='Black']")))
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f"Expected {expected_colors} did not match actual {actual_colors}"
