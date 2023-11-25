from behave import given, when, then

@given("Open target")
def open_target(context):
    context.app.product_search_results.open_target()


@when("Search for {product_name}")
def search_product(context, product_name):
    context.app.product_search_results.search_product(product_name)


@then("Verify product name and image")
def verify_product(context):
    context.app.product_search_results.verify_product()





