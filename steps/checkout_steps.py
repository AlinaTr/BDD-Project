from behave import *

@given('I am on the Checkout page')
def step_impl(context):
    context.checkout_page_object.navigate_to_checkout_1()

@when('I introduce the first name "{first_name}", last name "{last_name}", postal code "{post_code}"')
def step_impl(context, first_name, last_name, post_code):
    context.checkout_page_object.insert_first_name(first_name)
    context.checkout_page_object.insert_last_name(last_name)
    context.checkout_page_object.insert_postal_code(post_code)

@when('I click on continue button')
def step_impl(context):
    context.checkout_page_object.click_continue_button()

@when('I click on cancel button')
def step_impl(context):
    context.checkout_page_object.click_cancel_button()


@when('I have an overview on the products in my cart')
def step_impl(context):
    context.checkout_page_object.check_overview()

@when('I click on finish button')
def step_impl(context):
    context.checkout_page_object.click_finish_button()

@when('I am redirected to checkout step 2')
def step_impl(context):
    context.checkout_page_object.navigate_to_checkout_2()

@then('I am redirected to checkout step 2')
def step_impl(context):
    context.checkout_page_object.check_checkout_step2_url()

@then('I am redirected to shopping cart page')
def step_impl(context):
    context.shopping_cart_page_object.check_current_url()

@then('the order should be complete')
def step_impl(context):
    context.checkout_page_object.check_checkout_step3_page()

@then('I can see the confirmation message')
def step_impl(context):
    context.checkout_page_object.check_confirmation_message()




