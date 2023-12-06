from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

EMAIL_FIELD = (By.CSS_SELECTOR, "[id='username']")
PSWD_FIELD = (By.CSS_SELECTOR, "[id='password']")
SIGN_IN_BTN = (By.CSS_SELECTOR, "[id='login']")
ERROR_MSG = (By.CSS_SELECTOR, "[data-test*='AlertDisplay'] div")

@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()

@when('Store original windows')
def store_original_windows(context):
    context.windows = context.app.page.get_all_windows()
    context.original_window = context.app.page.get_current_window()

@when('Click on Target terms and conditions link')
def click_terms_and_conditions(context):
    context.app.sign_in_page.click_terms_and_conditions()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_tnc_page_is_opened(context):
    context.app.sign_in_page.verify_tnc_page_is_opened()



@then('User can close new window and switch back to original')
def close_new_window(context):
    context.app.page.close_page()
    context.app.page.switch_to_window(context.original_window)


@then('Verify Sign in page opened')
def verify_sign_in_page(context):
    context.app.sign_in_page.verify_sign_in_page_txt()


@when('Enter incorrect email and password combination')
def enter_incorrect_login(context):
    context.app.page.input('instantdriver135@gmail.com', *EMAIL_FIELD)
    context.app.page.input('idriver135', *PSWD_FIELD)
    sleep(3)


@when('Click login button')
def login(context):
    context.app.page.click(*SIGN_IN_BTN)
    sleep(3)


@then("Verify '{text}' message is shown")
def verify_message(context, text):
    context.app.page.verify_text(text, *ERROR_MSG)