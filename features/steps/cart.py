from behave import given, when, then

@then('Verify Cart has {amount} Item')
def verify_first_product_was_added(context, amount):
    context.app.cart_page.verify_first_product_was_added(amount)