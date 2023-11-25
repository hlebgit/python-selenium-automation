from behave import given, when, then

@given("Open target page")
def open_target_page(context):
    context.app.verify_cart_is_empty.open_target()


@when("Click on cart icon")
def search_product(context):
    context.app.verify_cart_is_empty.click_on_cart_icon()


@then("Verify Cart is Empty Message")
def verify_message(context):
    context.app.verify_cart_is_empty.verify_cart_is_empty_message()





