from behave import given, when, then

@given("Open product page")
def open_product_page(context):
    context.app.checkout_christmas_tree_product.open_christmas_tree_page()

@when("Add product to the cart")
def add_product(context):
    context.app.checkout_christmas_tree_product.add_product_to_the_cart()

@when("Check Out")
def checkout_cart(context):
    context.app.checkout_christmas_tree_product.checkout_cart()

@then("Verify title")
def view_cart_and_verify(context):
    context.app.checkout_christmas_tree_product.view_cart_and_verify()