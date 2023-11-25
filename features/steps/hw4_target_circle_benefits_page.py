from behave import given, when, then

@given("Open target circle page")
def open_target_circle_page(context):
    context.app.target_circle_benefits_page.open_target_circle_benefits_page()

@then("Verify user can see {number_of_benefits} benefits")
def verify_benefits(context, number_of_benefits):
    context.app.target_circle_benefits_page.verify_target_circle_benefits(number_of_benefits)
