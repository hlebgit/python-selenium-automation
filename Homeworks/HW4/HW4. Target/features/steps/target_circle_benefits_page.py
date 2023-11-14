from selenium.webdriver.common.by import By
from behave import given, when, then

@given("Open target circle page")
def open_targe(context):
    context.driver.get("https://www.target.com/circle")

@then("Verify user can see {number_of_benefits} benefits")
def verify_benefits(context, number_of_benefits):
    number_of_benefits = int(number_of_benefits)
    elements = context.driver.find_elements(By. CSS_SELECTOR, "[class*='BenefitsGrid'] li")
    assert len(elements) == number_of_benefits, f"Error: required benefits should be {number_of_benefits}, actual number is {len(elements)}!"
