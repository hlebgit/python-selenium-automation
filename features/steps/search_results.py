from behave import given, when, then

@when('Add first product of the search results to the cart')
def add_first_product_of_search_results_to_the_cart(context):
    context.app.search_results_page.add_first_product_of_search_results_to_the_cart()


@when('Checkout')
def click_view_cart_and_checkout(context):
    context.app.search_results_page.click_view_cart_and_checkout()