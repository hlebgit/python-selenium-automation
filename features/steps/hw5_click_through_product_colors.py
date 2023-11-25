from behave import given, when, then

@given("Open target page with product")
def open_product_page(context):
    context.app.click_through_colors.open_product_page()


@then("Verify user can click through colors")
def verify_colors(context):
    context.app.click_through_colors.verify_colors()
