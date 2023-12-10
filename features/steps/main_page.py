from behave import given, when, then


@given('Open Target page')
def open_target(context):
    context.app.main_page.open_main()

@when('Click sign in')
def click_sign_in(context):
    context.app.main_page.sign_in()


@when('Click sign in navigation menu')
def click_sign_in_in_nav_manu(context):
    context.app.main_page.sign_in_in_nav_manu()

@given('Open Target')
def open_target(context):
    context.app.main_page.open_main()

@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search_product_on_main_page(product)