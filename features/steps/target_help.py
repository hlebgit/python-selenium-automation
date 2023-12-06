from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PAGE_TITLE = (By.CSS_SELECTOR, "[id='pageTitle'] h1")

@given('Open Target help page')
def open_target_help_page(context):
    context.app.page.open_url("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")


@when('Click Browse Help dropdown and choose {topic}')
def click_browse_help_dropdown(context, topic):
    context.app.target_help_page.choose_help_dropdown_option(topic)


@then('Verify the Gift Cards page opened')
def verify_page(context):
    context.app.page.verify_text("Target GiftCard balance", *PAGE_TITLE)