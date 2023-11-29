from behave import given, when, then


@then("Verify product name and image")
def verify_product(context):
    context.app.product_search_results.verify_product()





