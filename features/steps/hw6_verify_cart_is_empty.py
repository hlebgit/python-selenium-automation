from behave import given, when, then


@when("Click on cart icon")
def search_product(context):
    context.app.verify_cart_is_empty.click_on_cart_icon()


@then("Verify Cart is Empty Message")
def verify_message(context):
    context.app.verify_cart_is_empty.verify_cart_is_empty_message()





